from crawler import BaseCrawler
from object import Building

sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class HouseholdPriceCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.region_code = None
        self.building_code = None

        self.sale_type = None

    def set_building_info(self, building: Building) -> None:
        self.region_code = building.region_code
        self.building_code = building.building_code

    def set_sale_type(self, sale_type: str) -> None:
        self.sale_type = sale_type

    def crawl(self, page_num) -> "json":
        url = self.household_list_url(page_num)
        json_response = self.send_request(url).json()

        return json_response

    def household_list_url(self, page_num: int) -> str:
        sale_type_code = sale_type_enum[self.sale_type]

        base_url = f"{self.baseURL}/getComplexArticleList?"
        region_url = f"hscpNo={self.building_code}&cortarNo={self.region_code}"
        detail_url = f"&tradTpCd={sale_type_code}&order=point_&showR0=N&page={page_num}"

        url = base_url + region_url + detail_url

        return url
