"""changed structure to accomodate security

Revision ID: 95a591d2d98e
Revises: b23656541c17
Create Date: 2021-12-10 06:32:58.080341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95a591d2d98e'
down_revision = 'b23656541c17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', table_args=(UniqueConstraint('email'))) as batch_op:
        batch_op.add_column('user', sa.Column('email', sa.String(length=250), nullable=True))
        batch_op.add_column('user', sa.Column('active', sa.Boolean(), nullable=True))
        batch_op.drop_index('ix_user_username')
        batch_op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.drop_column('user', 'active')
    op.drop_column('user', 'email')
    op.drop_table('roles_users')
    op.drop_table('role')
    # ### end Alembic commands ###
