import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass


@dataclass
class ProvinceModel:
    __tablename__ = "province"

    id = sa.Column(sa.Integer(), primary_key=True)

    sido = sa.Column(sa.String(20))
    gugun = sa.Column(sa.String(20))
    eupmyeondong = sa.Column(sa.String(20))
    dongli = sa.Column(sa.String(20))
