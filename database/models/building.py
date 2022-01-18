from .base import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import ENUM

class Building(Base):
    
    __tablename__ = "building"

    building_id = Column(Integer, primary_key=True, autoincrement=True)
    building_name = Column(String(50), nullable=False)
    building_type = Column(ENUM("APT", "OPT", name='building_type_enum'), nullable=False)
    total_household = Column(Integer, nullable=False)
    lowest_floor = Column(Integer, nullable=False)
    highest_floor = Column(Integer, nullable=False)
    approval_date = Column(Date, nullable=False)
    total_dong = Column(Integer, nullable=False)
    number_address = Column(String(100), nullable=False) # 지번주소
    road_address = Column(String(100), nullable=False)
    total_deal = Column(Integer, nullable=False)
    total_jeonse = Column(Integer, nullable=False)
    total_wolse = Column(Integer, nullable=False)

    # relationship
