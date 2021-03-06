import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.validator import ErrorHandler
from helpers.pagination.paginate import Paginate, validate_page
from api.block.models import Block
from api.floor.models import Floor as FloorModel
from api.room.models import Room as RoomModel
from api.room.schema import Room


class Floor(SQLAlchemyObjectType):
    class Meta:
        model = FloorModel


class CreateFloor(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        block_id = graphene.Int(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        get_block = Block.query.filter_by(id=kwargs['block_id']).first()
        if not get_block:
            raise GraphQLError("Block not found")
        query = Floor.get_query(info)
        query_block = query.join(Block.floors)

        admin_roles.create_floor_update_delete_block(kwargs['block_id'])
        result = query_block.filter(
            Block.id == kwargs['block_id'],
            FloorModel.name == kwargs.get('name').capitalize()
        )
        if result.count() > 0:
            ErrorHandler.check_conflict(self, kwargs['name'], 'Floor')

        floor = FloorModel(**kwargs)
        floor.save()
        return CreateFloor(floor=floor)


class UpdateFloor(graphene.Mutation):

    class Arguments:
        floor_id = graphene.Int(required=True)
        name = graphene.String(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, floor_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_floor = Floor.get_query(info)
        exact_floor = query_floor.filter(FloorModel.id == floor_id).first()
        if not exact_floor:
            raise GraphQLError("Floor not found")

        admin_roles.update_delete_floor(floor_id)
        result = query_floor.filter(
            FloorModel.block_id == exact_floor.block_id,
            FloorModel.name == kwargs.get('name').capitalize()
        )
        if result.count() > 0:
            ErrorHandler.check_conflict(self, kwargs['name'], 'Floor')

        update_entity_fields(exact_floor, **kwargs)
        exact_floor.save()
        return UpdateFloor(floor=exact_floor)


class DeleteFloor(graphene.Mutation):

    class Arguments:
        floor_id = graphene.Int(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, floor_id, **kwargs):
        query_floor = Floor.get_query(info)
        exact_floor = query_floor.filter(
            FloorModel.id == floor_id).first()
        if not exact_floor:
            raise GraphQLError("Floor not found")

        admin_roles.update_delete_floor(floor_id)
        exact_floor.delete()
        return DeleteFloor(floor=exact_floor)


class PaginatedFloors(Paginate):
    floors = graphene.List(Floor)

    def resolve_floors(self, info, **kwargs):
        ''' This function paginates the returned response
        if page parameter is passed,
        otherwise it returns all floors
        '''
        page = self.page
        per_page = self.per_page
        query = Floor.get_query(info)
        if not page:
            return query.all()
        page = validate_page(page)
        self.query_total = query.count()
        result = query.limit(per_page).offset(page*per_page)
        if result.count() == 0:
            return GraphQLError("No more resources")
        return result


class Query(graphene.ObjectType):
    all_floors = graphene.Field(
        PaginatedFloors,
        page=graphene.Int(),
        per_page=graphene.Int(),
        name=graphene.String()
    )
    get_rooms_in_a_floor = graphene.List(
        lambda: Room,
        floor_id=graphene.Int()
    )
    filter_by_block = graphene.List(Floor, blockId=graphene.Int())

    def resolve_all_floors(self, info, **kwargs):
        response = PaginatedFloors(**kwargs)
        return response

    def resolve_get_rooms_in_a_floor(self, info, floor_id):
        query = Room.get_query(info)
        rooms = query.filter(RoomModel.floor_id == floor_id)
        return rooms

    @Auth.user_roles('Admin')
    def resolve_filter_by_block(self, info, blockId):
        query = Floor.get_query(info)
        floors = query.filter_by(block_id=blockId)
        if floors.count() < 1:
            raise GraphQLError('Floors not found in this block')
        return floors


class Mutation(graphene.ObjectType):
    create_floor = CreateFloor.Field()
    update_floor = UpdateFloor.Field()
    delete_floor = DeleteFloor.Field()
