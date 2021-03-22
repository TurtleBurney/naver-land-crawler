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

    fields                DATA TYPE         INDEX   NULLABLE
        id              : Integer           PK      FALSE
        category        : Enum                      FALSE
        deal_upper      : Integer
        deal_lower      : Integer
        rent_upper      : Integer
        rent_lower      : Integer
    relationship
        Household       : household.id      FK       FALSE
    """

    # meta
    __tablename__ = "contract"
    id = sa.Column(sa.Integer(), primary_key=True)

    # fields
    category = sa.Column(
        sa.Enum(ContractCategory, name="en_contract_category"), nullable=False
    )
    deal_upper = sa.Column(sa.Integer())  # 거래가 상한
    deal_lower = sa.Column(sa.Integer())  # 거래가 하한
    rent_upper = sa.Column(sa.Integer())  # 월세 상한
    rent_lower = sa.Column(sa.Integer())  # 월세 하한

    # relationship
    household_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey("household.id", ondelete="CASCADE", name="household_fkey"),
        nullable=False,
        index=True,
    )
