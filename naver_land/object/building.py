import math

CONTRACT_COUNTS_PER_PAGE = 20


class Building:
    def __init__(self, data: dict, region_code: str, building_code: str):
        self.building_code = building_code
        self.region_code = region_code

        self.building_name = data["title"]["building_name"]

        self.total_household = data["detail"]["total_household"]
        self.total_dong = data["detail"]["total_dong"]
        self.approval_date = data["detail"]["approval_date"]

        self.lowest_floor = data["floor"]["lowest"]
        self.highest_floor = data["floor"]["highest"]

        self.land_address = data["address"]["land"]
        self.road_address = data["address"]["road"]

        self.deal_count = data["contract"]["deal"]
        self.jeonse_count = data["contract"]["jeonse"]
        self.wolse_count = data["contract"]["wolse"]

    def get_info(self) -> dict:
        return {
            "building_code": self.building_code,
            "region_code": self.region_code,
            "building_name": self.building_name,
            "total_household": self.total_household,
            "total_dong": self.total_dong,
            "approval_date": self.approval_date,
            "lowest_floor": self.lowest_floor,
            "highest_floor": self.highest_floor,
            "land_address": self.land_address,
            "road_address": self.road_address,
            "deal_count": self.deal_count,
            "jeonse_count": self.jeonse_count,
            "wolse_count": self.wolse_count,
        }

    def get_contract_count(self) -> dict:
        return {
            "deal_count": self.deal_count,
            "jeonse_count": self.jeonse_count,
            "wolse_count": self.wolse_count,
        }

    def get_household_page_num(self, sale_type) -> int:
        contract_info = self.get_contract_count()

        sale_type_count_key = sale_type + "_count"
        contract_count = contract_info[sale_type_count_key]

        pages = int(contract_count) / CONTRACT_COUNTS_PER_PAGE
        page_num = math.ceil(pages)

        return page_num

    def __repr__(self):
        return f"<building_code : {self.building_code}, building_name : {self.building_name}>"
