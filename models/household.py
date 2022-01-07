from sqlalchemy import orm
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import Float
from .base import Model, BaseModel


@dataclass
class Household(Model, BaseModel):
    """
    건물 세대 Info 모델

    fields                DATA TYPE         INDEX   NULLABLE
        id              : Integer           PK      FALSE
        dong            : Integer
        floor           : Integer
        ho              : String(32)
        window_side     : String(32)
    relationship
        Building        : building.id      FK       FALSE
        AreaType        : areatype.id      FK       FALSE
    backref
        Contract        : > this.id        > FK
    """

    # meta
    __tablename__ = "household"

    # fields
    id = Column(Integer(), primary_key=True)

    dong = Column(Integer())
    floor = Column(Integer())
    supply_area = Column(Float())  # 공급면적
    private_area = Column(Float())  # 전용면적
    window_side = Column(String(32))  # 방향(거실기준) 
    link = Column(String(200))  # 매물 링크

    # relationship
    building_id = Column(
        Integer(),
        ForeignKey("building.id", ondelete="CASCADE", name="building_fkey"),
        nullable=False,
        index=True,
    )
    areatype_id = Column(
        Integer(),
        ForeignKey("areatype.id", ondelete="CASCADE", name="areatype_fkey"),
        nullable=False,
        index=True,
    )

    # Backref
    # TODO : 외래키 관계 수정 필요
    contract = orm.relationship("Contract", backref=orm.backref("contract"))
