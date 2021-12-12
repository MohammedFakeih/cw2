"""added book description

Revision ID: 72acb03327ce
Revises: 7dca0b572853
Create Date: 2021-12-12 02:30:15.587939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72acb03327ce'
down_revision = '7dca0b572853'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'description')
    # ### end Alembic commands ###