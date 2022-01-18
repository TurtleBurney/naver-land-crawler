from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from dataclasses import dataclass
from .base import Base


@dataclass
class AreaType(Base):
    """
    건물 면적 타입 Info 모델

    fields                DATA TYPE         INDEX   NULLABLE
        id              : Integer           PK      FALSE
        area_name       : String(16)
        shared_area     : Float(decimal)
        exclusive_area  : Float(decimal)
    relationship
        Building        : building.id      FK       FALSE
    backref
        Household       : > this.id        > FK
    """

    # meta
    __tablename__ = "areatype"

    # fields
    id = Column(Integer(), primary_key=True)

    area_name = Column(String(16), nullable=False)
    shared_area = Column(Float(), nullable=False)
    exclusive_area = Column(Float(), nullable=False)

    # relationship
    building_id = Column(
        Integer(),
        ForeignKey("building.id", ondelete="CASCADE", name="building_fkey"),
        nullable=False,
        index=True,
    )

    # backref
    # TODO: backref name check
    household = orm.relationship("Household", backref=orm.backref("_household"))
