"""add missing responses table

Revision ID: d2a4ba0089fa
Revises: c772ffb07441
Create Date: 2019-01-15 11:55:06.795073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2a4ba0089fa'
down_revision = 'c772ffb07441'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.Column('check', sa.Boolean(), nullable=True),
    sa.Column('text_area', sa.String(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('missing_items',
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('response_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['resources.id'], ),
    sa.ForeignKeyConstraint(['response_id'], ['responses.id'], )
    )
    op.add_column('questions', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'is_active')
    op.drop_table('missing_items')
    op.drop_table('responses')
    # ### end Alembic commands ###
