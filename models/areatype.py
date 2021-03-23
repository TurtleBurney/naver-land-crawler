import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
from .base import Model, BaseModel


@dataclass
class AreaType(Model, BaseModel):
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
    id = sa.Column(sa.Integer(), primary_key=True)

    area_name = sa.Column(sa.String(16), nullable=False)
    shared_area = sa.Column(sa.Float(), nullable=False)
    exclusive_area = sa.Column(sa.Float(), nullable=False)

    # relationship
    building_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey("building.id", ondelete="CASCADE", name="building_fkey"),
        nullable=False,
        index=True,
    )

    # backref
    # TODO: backref name check
    household = orm.relationship("Household", backref=orm.backref("_household"))
