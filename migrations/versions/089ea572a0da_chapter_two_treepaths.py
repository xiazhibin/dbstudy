"""empty message

Revision ID: 089ea572a0da
Revises: 310453e642ca
Create Date: 2017-02-11 11:54:53.993337

"""

# revision identifiers, used by Alembic.
revision = '089ea572a0da'
down_revision = '310453e642ca'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tree_paths',
    sa.Column('ancestor', sa.BigInteger(), nullable=False),
    sa.Column('descendant', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['ancestor'], ['comments.comment_id'], ),
    sa.ForeignKeyConstraint(['descendant'], ['comments.comment_id'], ),
    sa.PrimaryKeyConstraint('ancestor', 'descendant')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tree_paths')
    # ### end Alembic commands ###
