"""add foreign-key to posts table

Revision ID: 90507b9ef109
Revises: 9704069f6b57
Create Date: 2022-05-12 10:24:41.455695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90507b9ef109'
down_revision = '9704069f6b57'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
