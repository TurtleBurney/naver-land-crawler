import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass


@dataclass
class ContractModel:
    __tablename__ = "contract"

    id = sa.Column(sa.Integer(), primary_key=True)

    building_id = sa.Integer()
    category = sa.Column(sa.String(100))

    trade_upper = sa.Column(sa.Integer())
    trade_lower = sa.Column(sa.Integer())

    deposit_upper = sa.Column(sa.Integer())
    deposit_lower = sa.Column(sa.Integer())

    rent_upper = sa.Column(sa.Integer())
    rent_lower = sa.Column(sa.Integer())
