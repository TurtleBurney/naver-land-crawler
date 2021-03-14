"""first

Revision ID: 3e3e5a4d16a6
Revises: 
Create Date: 2021-03-14 22:43:09.464972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3e3e5a4d16a6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "building_template",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(200)),
        sa.Column("category", sa.String(100)),
        sa.Column("traiding_num", sa.Integer),
        sa.Column("tenant_num", sa.Integer),
        sa.Column("wolse_num", sa.Integer),
    )


def downgrade():
    op.drop_table("building_template")
