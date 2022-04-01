import json

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
            household_info = self.parse_household_info(response.json(), page_num)
        return household_list

    def parse_household_info(self, response: json, page_num):
        household_raw_list = response["result"]["list"]
        household_data = []
        for i in range(20):
            household = household_raw_list[0]
            # TODO : 개별 매물 household같은 클래스로 담아 저장하기

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
