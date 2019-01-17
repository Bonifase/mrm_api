from sqlalchemy import (Column, String, Integer, ForeignKey, Table)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.notification.models import Notification  # noqa: F401
from api.feedback.models import Feedback  # noqa: F401
from api.response.models import Response  # noqa: F401

users_roles = Table(
    'users_roles',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    email = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=True)
    name = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    notification_settings = relationship(
        'Notification', cascade="all, delete-orphan")
    feedback = relationship('Feedback', cascade="all, delete-orphan")
    associated_roles = relationship(
        'Role', secondary="users_roles", backref=('users_association'), lazy="joined")

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.email = kwargs['email']
        self.name = kwargs['name']
        self.picture = kwargs['picture']
