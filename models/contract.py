import enum
import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass
from .base import Model, BaseModel


class ContractCategory(enum.Enum):
    DEAL = "매매"
    TNANT = "전세"
    RENT = "월세"


@dataclass
class Contract(Model, BaseModel):
    """
    계약 Info 모델
    """

    __tablename__ = "contract"

    id = sa.Column(sa.Integer(), primary_key=True)

    building_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey("building.id", ondelete="CASCADE", name="building_fkey"),
        nullable=False,
        index=True,
    )
    category = sa.Column(
        sa.Enum(ContractCategory, name="en_contract_category"), nullable=False
    )

    deal_upper = sa.Column(sa.Integer())
    deal_lower = sa.Column(sa.Integer())

    tnant_upper = sa.Column(sa.Integer())
    tnant_lower = sa.Column(sa.Integer())

    rent_upper = sa.Column(sa.Integer())
    rent_lower = sa.Column(sa.Integer())
