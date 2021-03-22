import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
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
    id = sa.Column(sa.Integer(), primary_key=True)

    # fields
    dong = sa.Column(sa.Integer())
    floor = sa.Column(sa.Integer())
    ho = sa.Column(sa.String(32))
    window_side = sa.Column(sa.String(32))

    # relationship
    building_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey("building.id", ondelete="CASCADE", name="building_fkey"),
        nullable=False,
        index=True,
    )
    areatype_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey("areatype.id", ondelete="CASCADE", name="areatype_fkey"),
        nullable=False,
        index=True,
    )

    # Backref
    contract = orm.relationship("Contract", backref=orm.backref("contract"))
