import enum
from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import ForeignKey
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
        deposit_upper   : Integer
        deposit_lower   : Integer
        rent_upper      : Integer
        rent_lower      : Integer
    relationship
        Household       : household.id      FK       FALSE
    """

    # meta
    __tablename__ = "contract"

    # fields
    id = Column(Integer(), primary_key=True)

    category = Column(
        Enum(ContractCategory, name="en_contract_category"), nullable=False
    )
    deal_upper = Column(Integer())  # 거래가 상한
    deal_lower = Column(Integer())  # 거래가 하한
    deposit_upper = Column(Integer())  # 보증금 상한
    deposit_lower = Column(Integer())  # 보증금 하한
    rent_upper = Column(Integer())  # 월세 상한
    rent_lower = Column(Integer())  # 월세 하한

    # relationship
    household_id = Column(
        Integer(),
        ForeignKey("household.id", ondelete="CASCADE", name="household_fkey"),
        nullable=False,
        index=True,
    )
