from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models import Base


class Building(Base):
    __tablename__ = "building"

    building_id = Column(String(50), primary_key=True)

    building_name = Column(String(50), nullable=False)
    building_type = Column(
        Enum("APT", "OPT", name="building_type_enum"), nullable=False
    )

    dong_count = Column(Integer, nullable=False)
    household_count = Column(Integer, nullable=False)
    approval_date = Column(Date, nullable=False)

    lowest_floor = Column(Integer, nullable=False)
    highest_floor = Column(Integer, nullable=False)

    land_address = Column(String(100), nullable=False)
    road_address = Column(String(100), nullable=False)

    deal_count = Column(Integer, default=0)
    jeonse_count = Column(Integer, default=0)
    wolse_count = Column(Integer, default=0)

    # Foreign Key
    fk_region_code = Column(
        String(50), ForeignKey("region.region_code", ondelete="CASCADE")
    )

    # Back Reference
    households = relationship("Household", backref="building")
