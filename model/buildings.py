import sqlalchemy as sa
from sqlalchemy import orm
from dataclasses import dataclass


@dataclass
class Building:
    building_name: str
    building_type: str
    # contract_type : str
    trading_num: int
    tenant_num: int
    wolse_num: int
    # building_dong : str
    # exclusive_area : float
    # shared_area : float
    # target_floor : int
    # max_floor : int
    # window_side : str
    # trading_price_min : int
    # trading_price_max : int


@dataclass
class BuildingTemplateModel:
    __tablename__ = "building_template"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(200))
    category = sa.Column(sa.String(100))
    traiding_num = sa.Column(sa.Integer)
    tenant_num = sa.Column(sa.Integer)
    wolse_num = sa.Column(sa.Integer)
