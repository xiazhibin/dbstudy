"""init db

Revision ID: 55d4541fd269
Revises: None
Create Date: 2017-02-06 21:26:54.324260

"""

# revision identifiers, used by Alembic.
revision = '55d4541fd269'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
                    sa.Column('account_id', sa.BigInteger(), nullable=False),
                    sa.Column('first_name', sa.String(length=20), nullable=True),
                    sa.Column('account_name', sa.String(length=20), nullable=True),
                    sa.Column('last_name', sa.String(length=20), nullable=True),
                    sa.Column('password_hash', sa.String(length=64), nullable=True),
                    sa.Column('email', sa.String(length=100), nullable=True),
                    sa.PrimaryKeyConstraint('account_id')
                    )
    op.create_table('bug_status',
                    sa.Column('status', sa.String(length=20), nullable=False),
                    sa.PrimaryKeyConstraint('status')
                    )
    op.create_table('bugs',
                    sa.Column('bug_id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('summary', sa.String(length=80), nullable=True),
                    sa.Column('description', sa.String(length=1000), nullable=True),
                    sa.Column('resolution', sa.String(length=1000), nullable=True),
                    sa.Column('reported_by', sa.BigInteger(), nullable=True),
                    sa.Column('assigned_to', sa.BigInteger(), nullable=True),
                    sa.Column('verified_by', sa.BigInteger(), nullable=True),
                    sa.Column('status', sa.String(length=20), nullable=True),
                    sa.Column('priority', sa.String(length=20), nullable=True),
                    sa.Column('hours', sa.Numeric(precision=9, scale=2), nullable=True),
                    sa.PrimaryKeyConstraint('bug_id')
                    )
    op.create_table('products',
                    sa.Column('product_id', sa.BigInteger(), nullable=False),
                    sa.Column('product_name', sa.VARCHAR(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('product_id')
                    )
    op.create_table('bugs_products',
                    sa.Column('product_id', sa.BigInteger(), nullable=False),
                    sa.Column('bug_id', sa.BigInteger(), nullable=False),
                    sa.ForeignKeyConstraint(['bug_id'], ['bugs.bug_id'], ),
                    sa.PrimaryKeyConstraint('product_id', 'bug_id')
                    )
    op.create_table('comments',
                    sa.Column('comment_id', sa.BigInteger(), nullable=False),
                    sa.Column('bug_id', sa.BigInteger(), nullable=True),
                    sa.Column('author', sa.BigInteger(), nullable=True),
                    sa.Column('comment_at', sa.DateTime(), nullable=True),
                    sa.Column('comment', sa.Text(), nullable=True),
                    sa.ForeignKeyConstraint(['author'], ['accounts.account_id'], ),
                    sa.ForeignKeyConstraint(['bug_id'], ['bugs.bug_id'], ),
                    sa.PrimaryKeyConstraint('comment_id')
                    )
    op.create_table('screenshots',
                    sa.Column('image_id', sa.BigInteger(), nullable=False),
                    sa.Column('bug_id', sa.BigInteger(), nullable=False),
                    sa.Column('screenshot_image', sa.LargeBinary(), nullable=True),
                    sa.Column('caption', sa.VARCHAR(length=100), nullable=True),
                    sa.ForeignKeyConstraint(['bug_id'], ['bugs.bug_id'], ),
                    sa.PrimaryKeyConstraint('image_id', 'bug_id')
                    )
    op.create_table('tags',
                    sa.Column('bug_id', sa.BigInteger(), nullable=False),
                    sa.Column('tag', sa.VARCHAR(length=20), nullable=False),
                    sa.ForeignKeyConstraint(['bug_id'], ['bugs.bug_id'], ),
                    sa.PrimaryKeyConstraint('bug_id', 'tag')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('screenshots')
    op.drop_table('comments')
    op.drop_table('bugs_products')
    op.drop_table('products')
    op.drop_table('bugs')
    op.drop_table('bug_status')
    op.drop_table('accounts')
    # ### end Alembic commands ###
