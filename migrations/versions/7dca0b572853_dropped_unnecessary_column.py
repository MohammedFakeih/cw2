"""dropped unnecessary column

Revision ID: 7dca0b572853
Revises: 95a591d2d98e
Create Date: 2021-12-11 04:09:19.386159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dca0b572853'
down_revision = '95a591d2d98e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', table_args=(sa.UniqueConstraint('username'))) as batch_op:
        batch_op.drop_column('booksRead')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('booksRead', sa.INTEGER(), nullable=True))
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    # ### end Alembic commands ###