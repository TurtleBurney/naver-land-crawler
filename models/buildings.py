import enum

import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from .base import Model, BaseModel


class BuildingCategory(enum.Enum):
    APARTMENT = "APT"
    OFFICETEL = "OPT"


@dataclass
class Building(Model, BaseModel):
    """
    건물 Info 모델
    """

    __tablename__ = "building"

    id = sa.Column(sa.Integer(), primary_key=True)

    province_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey("province.id", ondelete="CASCADE", name="province_fkey"),
        nullable=False,
        index=True,
    )

    name = sa.Column(sa.String(256), nullable=False, index=True)
    category = sa.Column(
        sa.Enum(BuildingCategory, name="en_building_category"), nullable=False
    )

    dong = sa.Column(sa.String(64))
    ho = sa.Column(sa.String(64))

    floor = sa.Column(sa.Integer)
    max_floor = sa.Column(sa.Integer)

    exclusive_area = sa.Column(sa.Float(asdecimal=True), nullable=False)
    shared_area = sa.Column(sa.Float(asdecimal=True))
    window_side = sa.Column(sa.String(64))

    contracts = orm.relationship("Contract", backref=orm.backref("contract"))
