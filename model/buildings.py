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
