"""message&comment manage

Revision ID: fa4db43bbfa9
Revises: 904375a6a656
Create Date: 2019-04-20 09:06:56.472514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa4db43bbfa9'
down_revision = '904375a6a656'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('hide', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('hide', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'hide')
    op.drop_column('comments', 'hide')
    # ### end Alembic commands ###
