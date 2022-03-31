from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.models import Base


class Region(Base):
    __tablename__ = "region"

    region_code = Column(String(50), primary_key=True)

    city = Column(String(10), nullable=False)
    gu = Column(String(10), nullable=True)
    dong = Column(String(10), nullable=True)

    parent_region_code = Column(String(50), nullable=True)

    # Back Reference
    buildings = relationship("Building", backref="region")
