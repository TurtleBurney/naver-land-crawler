import enum
from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import ForeignKey
from dataclasses import dataclass

from sqlalchemy.sql.expression import null
from .base import Model, BaseModel


class ContractCategory(enum.Enum):
    DEAL = "매매"
    TNANT = "전세"
    RENT = "월세"


@dataclass
class Price(Model, BaseModel):
    """
    매물 가격 Info 모델 (단위 : 만원)

    fields                DATA TYPE         INDEX   NULLABLE
        id              : Integer           PK      FALSE
        contract_type   : Enum                      FALSE
        base_price      : Integer                   FALSE
        higher_price    : Integer                   TRUE   
        monthly_rent    : Integer                   TRUE<조건부>
    relationship
        Household       : household.id      FK      FALSE
    """

    # meta
    __tablename__ = "price"

    # fields
    id = Column(Integer(), primary_key=True)

    contract_type = Column(
        Enum(ContractCategory, name="en_contract_category"), nullable=False
    )
    base_price = Column(Integer())  # 거래가 상한
    higher_price = Column(Integer(), nullable=True)  # 거래가 하한
    monthly_rent = Column(Integer(), nullable=True)  # 보증금 상한

    # relationship
    household_id = Column(
        Integer(),
        ForeignKey("household.id", ondelete="CASCADE", name="household_fkey"),
        nullable=False,
        index=True,
    )
