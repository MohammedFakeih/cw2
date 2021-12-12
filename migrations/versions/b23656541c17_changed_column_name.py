"""changed column name

Revision ID: b23656541c17
Revises: d90842d3d1d5
Create Date: 2021-12-10 03:28:38.851430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b23656541c17'
down_revision = 'd90842d3d1d5'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('review', 'isReading', new_column_name='isFinished')


def downgrade():
    op.alter_column('review', 'isFinished', new_column_name='isReading')
