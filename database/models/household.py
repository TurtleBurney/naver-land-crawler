from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from models import Base


class Household(Base):
    __tablename__ = "household"

    household_id = Column(Integer, primary_key=True, autoincrement=True)

    building_dong = Column(String(10), nullable=False)
    floor = Column(Integer, nullable=False)
    direction = Column(String(10), nullable=False)

    supply_area = Column(Float, nullable=False)
    private_area = Column(Float, nullable=False)

    household_url = Column(String(200), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_onupdate=func.now())

    # Foreign key
    fk_building_id = Column(
        String(50), ForeignKey("building.building_id", ondelete="CASCADE")
    )

    # Back Reference
    contract_prices = relationship("ContractPrice", backref="household")
