"""add is_activated for user

Revision ID: 4783fc4800b4
Revises: cf81f4f7c9e8
Create Date: 2023-03-07 20:58:49.409842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4783fc4800b4'
down_revision = 'cf81f4f7c9e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_activated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_activated')
    # ### end Alembic commands ###