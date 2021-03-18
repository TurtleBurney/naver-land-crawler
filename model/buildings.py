import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass


@dataclass
class BuildingModel:
    __tablename__ = "building"

    id = sa.Column(sa.Integer(), primary_key=True)

    province_id = sa.Integer()
    name = sa.Column(sa.String(256))
    category = sa.Column(sa.String(100))

    dong = sa.Column(sa.String(64))
    ho = sa.Column(sa.String(64))

    floor = sa.Column(sa.Integer)
    max_floor = sa.Column(sa.Integer)

    exclusive_area = sa.Column(sa.Float())
    shared_area = sa.Column(sa.Float())
    window_side = sa.Colum(sa.String(64))
