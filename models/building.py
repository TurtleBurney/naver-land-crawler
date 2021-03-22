import enum

import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
from .base import Model, BaseModel


class BuildingCategory(enum.Enum):
    APARTMENT = "APT"
    OFFICETEL = "OPT"


@dataclass
class Building(Model, BaseModel):
    """
    건물 Info 모델

    fields                DATA TYPE         INDEX   NULLABLE
        id              : Integer           PK      FALSE
        name            : String(256)               FALSE
        category        : Enum                      FALSE
        built_year      : Integer
        total_dong      : Integer
        total_houshold  : Integer
        land_address    : String(128)
        road_address    : String(128)
        deal_count      : Integer
        tnant_count     : Integer
        rent_count      : Integer
    relation
        AreaType        : this.id           FK
        HouseHold       : this.id           FK
    """

    # metadata
    __tablename__ = "building"

    # fields
    id = sa.Column(sa.Integer(), primary_key=True)

    name = sa.Column(sa.String(256), nullable=False, index=True)  # 건축물 명
    category = sa.Column(
        sa.Enum(BuildingCategory, name="en_building_category"), nullable=False
    )  # 건축물 종류

    built_year = sa.Column(sa.Integer())  # 사용승인일(건축년도)
    total_dong = sa.Column(sa.Integer())  # 전체 동수
    total_household = sa.Column(sa.Integer())  # 총 세대수

    land_address = sa.String(128)  # 지번 주소
    road_address = sa.String(128)  # 도로명 주소

    deal_count = sa.Integer()  # 현재 매물(매매)의 수
    tnant_count = sa.Integer()  # 현재 매물(전세)의 수
    rent_count = sa.Integer()  # 현재 매물(월세)의 수

    # relationship
    area_type = orm.relationship("AreaType", backref=orm.backref("area_type"))
    household = orm.relationship("Household", backref=orm.backref("household"))
