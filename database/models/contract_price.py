from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from database.models import Base


class ContractPrice(Base):
    __tablename__ = "contractprice"

    contract_price_id = Column(Integer, primary_key=True, autoincrement=True)
    contract_type = Column(
        Enum("DEAL", "JEONSE", "WOLSE", name="contract_type_enum"), nullable=False
    )

    # 단위 : 만 원
    min_price = Column(String(10), nullable=False)
    max_price = Column(String(10), nullable=False)
    wolse_price = Column(String(10), nullable=True)

    # Foreign Key
    fk_household_id = Column(
        Integer, ForeignKey("household.household_id", ondelete="CASCADE")
    )
