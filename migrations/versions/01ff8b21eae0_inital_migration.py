"""inital migration

Revision ID: 01ff8b21eae0
Revises: 
Create Date: 2021-12-10 01:03:56.932093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01ff8b21eae0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('author', sa.String(length=250), nullable=True),
    sa.Column('image', sa.String(length=250), nullable=True),
    sa.Column('avgRating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_author'), 'book', ['author'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('booksRead', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('review',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('bookId', sa.Integer(), nullable=False),
    sa.Column('userRating', sa.Integer(), nullable=True),
    sa.Column('startReading', sa.DateTime(), nullable=True),
    sa.Column('finishReading', sa.DateTime(), nullable=True),
    sa.Column('review', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['bookId'], ['book.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('userId', 'bookId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_author'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
