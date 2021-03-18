import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
from .base import Model, BaseModel


@dataclass
class Province(Model, BaseModel):
    __tablename__ = "province"

    id = sa.Column(sa.Integer(), primary_key=True)

    sido = sa.Column(sa.String(32))
    gugun = sa.Column(sa.String(32))
    eupmyeondong = sa.Column(sa.String(32))
    dongli = sa.Column(sa.String(32))

    buildings = orm.relationship("Building", backref=orm.backref("building"))
