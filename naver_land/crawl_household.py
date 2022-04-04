import json
from pprint import pprint
from base_crawler import BaseCrawler
from object import Building, Household

sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class HouseholdCrawler(BaseCrawler):
    def __init__(self, building: Building):
        super().__init__()
        self.building_code = building.building_code
        self.region_code = building.region_code
        self.contract_cnt = building.get_contract_info()

    def run(self):
        pass

    def get_household_list(self):
        sample_sale_type = sale_type_enum["deal"]
        household_list = []
        # 한 페이지당 20개의 매물 존재
        total_page_num = (int(self.contract_cnt["deal_count"]) // 20) + 1

        for page_num in range(1, total_page_num + 1):
            url = self.household_list_url(sample_sale_type, page_num)
            response = self.get_request(url)

            self.save_household_info(response.json(), page_num)

            household_info = self.parse_household_info(response.json(), page_num)
            household_list += household_info
        return household_list

    def parse_household_info(self, response: json, page_num):
        household_raw_list = response["result"]["list"]
        household_info = []

        iter_count = 20
        if page_num == int(self.contract_cnt["deal_count"]) // 20 + 1:
            iter_count = int(self.contract_cnt["deal_count"]) % 20

        for i in range(iter_count):
            household_raw = household_raw_list[i]

            household_data = {
                "building_dong": household_raw["bildNm"][:-1],
                "floor": household_raw["flrInfo"],
                "direction": household_raw["direction"],
                "supply_area": household_raw["spc1"],
                "private_area": household_raw["spc2"],
            }
            household = Household(household_data, self.building_code)
            household_info.append(household)
        return household_info

    def save_household_info(self, response: json, page_num):
        with open(f"./temp_household_{page_num}.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(response, ensure_ascii=False, indent="\t"))

    def household_list_url(self, sale_type: str, page_num):
        household_base_url = f"{self.baseURL}/getComplexArticleList?"
        household_region_url = (
            f"hscpNo={self.building_code}&cortarNo={self.region_code}"
        )
        household_detail_url = (
            f"&tradTpCd={sale_type}&order=point_&showR0=N&page={page_num}"
        )
        return household_base_url + household_region_url + household_detail_url
