"""create notes table

Revision ID: c09f4cf98eb8
Revises: 
Create Date: 2022-05-15 18:17:39.849302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09f4cf98eb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # pass
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade():
    # pass
    op.drop_table("notes")