"""
Base Model

"""
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


"""
TestModel

"""
class RegionTest(Base):
    __tablename__ = 'region_test'

    region_code = sql.Column(sql.String(50), primary_key=True)

    city = sql.Column(sql.String(50), nullable=False)
    gu = sql.Column(sql.String(10))
    dong = sql.Column(sql.String(10))

    parent_code = sql.Column(sql.String(50))
