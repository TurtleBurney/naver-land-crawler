from crawler import BaseCrawler
from object import Building

ITEM_COUNT_PER_REQUEST = 20
sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class HouseholdPriceResponse(BaseCrawler):
    def __init__(self, building: Building, sale_type: str):
        super().__init__()
        self.region_code = building.region_code
        self.building_code = building.building_code

        self.contract_cnt = building.get_contract_info()

        self.sale_type = sale_type

    def get_response_json(self, page_num: int) -> "json":
        url = self.household_list_url(sale_type_enum[self.sale_type], page_num)

        response = self.get_request(url)
        return response.json()

    def household_list_url(self, sale_type: str, page_num: int) -> str:
        household_base_url = f"{self.baseURL}/getComplexArticleList?"

        household_region_url = (
            f"hscpNo={self.building_code}&cortarNo={self.region_code}"
        )
        household_detail_url = (
            f"&tradTpCd={sale_type}&order=point_&showR0=N&page={page_num}"
        )
        return household_base_url + household_region_url + household_detail_url

    # Building에서 거래 방식에 따른 매물 개수 찾을때의 키 형성
    def add_str_count(self, sale_type: str) -> str:
        return sale_type + "_count"

    def calculate_total_page_num(self, sale_type_key: str) -> int:
        total_page_num = (
            int(self.contract_cnt[sale_type_key]) // ITEM_COUNT_PER_REQUEST
        ) + 1
        return total_page_num
