"""removed unique username index

Revision ID: 7abd048397f9
Revises: 72acb03327ce
Create Date: 2021-12-12 03:24:25.418637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7abd048397f9'
down_revision = '72acb03327ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_username', table_name='user')
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    # ### end Alembic commands ###
