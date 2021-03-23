import enum

import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
from .base import Model, BaseModel


mapper_registry = registry()


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
        total_household : Integer
        land_address    : String(128)
        road_address    : String(128)
        deal_count      : Integer
        tnant_count     : Integer
        rent_count      : Integer
    relation
        AreaType        : this.id           FK
        Household       : this.id           FK
    """

    # metadata
    __table__ = sa.Table(
        "building",
        mapper_registry.metadata,
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(256), nullable=False, index=True),  # 건축물 명
        sa.Column(
            "category",
            sa.Enum(BuildingCategory, name="en_building_category"),
            nullable=False,
        ),  # 건축물 종류
        sa.Column("built_year", sa.Integer()),  # 사용승인일(건축년도)
        sa.Column("total_dong", sa.Integer()),  # 전체 동수
        sa.Column("total_household", sa.Integer()),  # 총 세대수
        sa.Column("land_address", sa.String(128)),  # 지번 주소
        sa.Column("road_address", sa.String(128)),  # 도로명 주소
        sa.Column("deal_count", sa.Integer()),  # 현재 매물(매매)의 수
        sa.Column("tnant_count", sa.Integer()),  # 현재 매물(전세)의 수
        sa.Column("rent_count", sa.Integer()),  # 현재 매물(월세)의 수
    )

    # fields
    id: int
    name: str
    category: BuildingCategory
    built_year: int = None
    total_dong: int = None
    total_household: int = None

    land_address: str = None
    road_address: str = None

    deal_count: int = None
    tnant_count: int = None
    rent_count: int = None

    # relationship
    area_type = orm.relationship("AreaType", backref=orm.backref("areatype"))
    household = orm.relationship("Household", backref=orm.backref("household"))
