"""add content column to posts table

Revision ID: be0bb5b46552
Revises: 41e3278fe390
Create Date: 2022-05-12 10:11:04.349716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be0bb5b46552'
down_revision = '41e3278fe390'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
