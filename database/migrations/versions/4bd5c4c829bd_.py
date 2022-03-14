"""empty message

Revision ID: 4bd5c4c829bd
Revises: b1e305e5c537
Create Date: 2022-03-14 16:19:07.370338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bd5c4c829bd'
down_revision = 'b1e305e5c537'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contract_price', sa.Column('fk_household_id', sa.Integer(), nullable=True))
    op.drop_constraint('contract_price_fk_house_id_fkey', 'contract_price', type_='foreignkey')
    op.create_foreign_key(None, 'contract_price', 'household', ['fk_household_id'], ['household_id'], ondelete='CASCADE')
    op.drop_column('contract_price', 'fk_house_id')
    op.execute("ALTER TYPE contract_type_enum RENAME VALUE 'Deal' TO 'DEAL'")
    op.execute("ALTER TYPE contract_type_enum RENAME VALUE 'Jeonse' TO 'JEONSE'")
    op.execute("ALTER TYPE contract_type_enum RENAME VALUE 'Wolse' TO 'WOLSE'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE contract_type_enum RENAME VALUE 'WOLSE' TO 'Wolse'")
    op.execute("ALTER TYPE contract_type_enum RENAME VALUE 'JEONSE' TO 'Jeonse'")
    op.execute("ALTER TYPE contract_type_enum RENAME VALUE 'DEAL' TO 'Deal'")
    op.add_column('contract_price', sa.Column('fk_house_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint('contract_price_fk_household_id_fkey', 'contract_price', type_='foreignkey')
    op.create_foreign_key('contract_price_fk_house_id_fkey', 'contract_price', 'household', ['fk_house_id'], ['household_id'], ondelete='CASCADE')
    op.drop_column('contract_price', 'fk_household_id')
    # ### end Alembic commands ###
