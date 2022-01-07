import enum
from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Enum
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
    __tablename__ = "building"

    id = Column(Integer(), primary_key=True)
    name = Column(String(256), nullable=False, index=True)
    category = Column(
        Enum(BuildingCategory, name="en_building_category"),
        nullable=False,
    )
    built_year = Column(Integer())  # 사용승인일(건축년도)
    lowest_floor = Column(Integer())  # 최저층
    highest_floor = Column(Integer())  # 최고층
    total_dong = Column(Integer())  # 전체 동수
    total_household = Column(Integer())  # 총 세대수
    land_address = Column(String(128))  # 지번 주소
    road_address = Column(String(128))  # 도로명 주소
    deal_count = Column(Integer())  # 현재 매물(매매)의 수
    tnant_count = Column(Integer())  # 현재 매물(전세)의 수
    rent_count = Column(Integer())  # 현재 매물(월세)의 수

    # relationship
    area_type = orm.relationship("AreaType", backref=orm.backref("areatype"))
    household = orm.relationship("Household", backref=orm.backref("household"))
