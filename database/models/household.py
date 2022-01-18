from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func

class Household(Base):
    
    __tablename__ = "household"

    household_id = Column(Integer, primary_key=True, autoincrement=True)
    dong = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    direction = Column(String(10), nullable=False)
    area = Column(Float, nullable=False)
    link = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # relationship
