"""empty message

Revision ID: 557eacd526be
Revises: 
Create Date: 2022-02-07 18:41:25.587418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557eacd526be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('building',
    sa.Column('building_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('building_name', sa.String(length=50), nullable=False),
    sa.Column('building_type', sa.Enum('APT', 'OPT', name='building_type_enum'), nullable=False),
    sa.Column('total_household', sa.Integer(), nullable=False),
    sa.Column('lowest_floor', sa.Integer(), nullable=False),
    sa.Column('highest_floor', sa.Integer(), nullable=False),
    sa.Column('approval_date', sa.Date(), nullable=False),
    sa.Column('total_dong', sa.Integer(), nullable=False),
    sa.Column('number_address', sa.String(length=100), nullable=False),
    sa.Column('road_address', sa.String(length=100), nullable=False),
    sa.Column('total_deal', sa.Integer(), nullable=False),
    sa.Column('total_jeonse', sa.Integer(), nullable=False),
    sa.Column('total_wolse', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('building_id')
    )
    op.create_table('household',
    sa.Column('household_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dong', sa.Integer(), nullable=False),
    sa.Column('floor', sa.Integer(), nullable=False),
    sa.Column('direction', sa.String(length=10), nullable=False),
    sa.Column('area', sa.Float(), nullable=False),
    sa.Column('link', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('building_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['building_id'], ['building.building_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('household_id')
    )
    op.create_table('price',
    sa.Column('price_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sale_type', sa.Enum('Deal', 'Jeonse', 'Wolse', name='sale_type_enum'), nullable=False),
    sa.Column('default_price', sa.Integer(), nullable=False),
    sa.Column('highest_price', sa.Integer(), nullable=True),
    sa.Column('wolse_price', sa.Integer(), nullable=True),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['household.household_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('price_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('price')
    op.drop_table('household')
    op.drop_table('building')
    # ### end Alembic commands ###