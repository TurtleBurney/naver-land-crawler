from crawler.base import BaseCrawler
from object import Household

sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class HouseholdCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.region_code = None
        self.building_code = None

        self.sale_type_code = None

    def set_building_info(self, region_code: str, building_code: str) -> None:
        self.region_code = region_code
        self.building_code = building_code

    def set_sale_type(self, sale_type: str) -> None:
        sale_type_code = {
            "deal": "A1",
            "jeonse": "B1",
            "wolse": "B2",
        }[sale_type]

        self.sale_type_code = sale_type_code

    def crawl(self, page_num: int) -> list:
        # Step 1
        url = self.household_list_url(page_num)
        json_response = self.send_request(url).json()

        household_raw_list = json_response["result"]["list"]
        households = []

        # Step 2
        for household_raw in household_raw_list:
            household_data = {
                "household_code": household_raw["atclNo"],
                "building_dong": household_raw["bildNm"][:-1],
                "floor": household_raw["flrInfo"],
                "direction": household_raw["direction"],
                "supply_area": household_raw["spc1"],
                "private_area": household_raw["spc2"],
            }
            household = Household(household_data, self.building_code)
            households.append(household)

        return households

    def household_list_url(self, page_num: int) -> str:
        base_url = f"{self.naverURL}/complex/getComplexArticleList?"
        region_url = f"hscpNo={self.building_code}&cortarNo={self.region_code}"
        detail_url = (
            f"&tradTpCd={self.sale_type_code}&order=point_&showR0=N&page={page_num}"
        )

        url = base_url + region_url + detail_url

        return url
