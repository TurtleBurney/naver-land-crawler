from .base import Base
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import func

class Price(Base):
    
    __tablename__ = "price"

    price_id = Column(Integer, primary_key=True, autoincrement=True)
    sale_type = Column(ENUM("Deal", "Jeonse", "Wolse", name='sale_type_enum'), nullable=False)
    default_price = Column(Integer, nullable=False)
    highest_price = Column(Integer, nullable=True)
    wolse_price = Column(Integer, nullable=True)

    # relationship
