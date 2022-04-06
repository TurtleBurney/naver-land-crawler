import json
from base_crawler import BaseCrawler
from object import Building, Household

ITEM_COUNT_PER_REQUEST = 20
# TODO : enum class 생성해 관리
sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class HouseholdCrawler(BaseCrawler):
    def __init__(self, building: Building):
        super().__init__()
        self.building_code = building.building_code
        self.region_code = building.region_code
        self.contract_cnt = building.get_contract_info()

    def run(self) -> list:
        total_households = []

        for sale_type in sale_type_enum:
            print(f"{sale_type} 시작")
            total_households += self.get_household_list(sale_type)
            print(f"{sale_type} 종료")
        return total_households

    def get_household_list(self, sale_type: str) -> list:
        household_list = []

        # 한 페이지당 20개의 매물 존재
        sale_type_count = self.add_str_count(sale_type)
        total_page_num = (
            int(self.contract_cnt[sale_type_count]) // ITEM_COUNT_PER_REQUEST
        ) + 1

        for page_num in range(1, total_page_num + 1):
            url = self.household_list_url(sale_type_enum[sale_type], page_num)
            response = self.get_request(url)

            iter_count = self.calculate_iter_count(page_num, sale_type)

            household_info = self.parse_household_info(response.json(), iter_count)
            household_list += household_info
        return household_list

    # Building에서 거래 방식에 따른 매물 개수 찾을때의 키 형성
    def add_str_count(self, sale_type: str) -> str:
        return sale_type + "_count"

    # 20개 다 안 도는 경우 있어 iter_count 지정
    def calculate_iter_count(self, page_num: int, sale_type: str) -> int:
        iter_count = ITEM_COUNT_PER_REQUEST
        sale_type_count = self.add_str_count(sale_type)

        if (
            page_num
            == int(self.contract_cnt[sale_type_count]) // ITEM_COUNT_PER_REQUEST + 1
        ):
            iter_count = (
                int(self.contract_cnt[sale_type_count]) % ITEM_COUNT_PER_REQUEST
            )
        return iter_count

    def parse_household_info(self, response: json, iter_count: int) -> list:
        household_raw_list = response["result"]["list"]
        household_info = []

        for i in range(iter_count):
            household_raw = household_raw_list[i]

            household_data = {
                "household_code": household_raw["atclNo"],
                "building_dong": household_raw["bildNm"][:-1],
                "floor": household_raw["flrInfo"],
                "direction": household_raw["direction"],
                "supply_area": household_raw["spc1"],
                "private_area": household_raw["spc2"],
            }

            household = Household(household_data, self.building_code)
            household_info.append(household)
        return household_info

    def save_household_info(self, response: json, page_num: int) -> None:
        with open(f"./temp_household_{page_num}.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(response, ensure_ascii=False, indent="\t"))

    def household_list_url(self, sale_type: str, page_num: int) -> str:
        household_base_url = f"{self.baseURL}/getComplexArticleList?"
        household_region_url = (
            f"hscpNo={self.building_code}&cortarNo={self.region_code}"
        )
        household_detail_url = (
            f"&tradTpCd={sale_type}&order=point_&showR0=N&page={page_num}"
        )
        return household_base_url + household_region_url + household_detail_url
