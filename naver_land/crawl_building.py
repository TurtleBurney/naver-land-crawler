from base_crawler import BaseCrawler

from object.refiner import Refiner
from object.building import Building


class BuildingCrawler(BaseCrawler):
    def __init__(self, region_code: str):
        super.__init__(self)
        self.region_code = region_code
        # 이 코드를 가지고 있어야 하는가??

    def run(self):
        building_list = self.get_building_list(self.region_code)

        sample_building = building_list["result"][0]
        sample_building_id = sample_building["hscpNo"]  # 110209
        target_html = self.get_building_detail_html(sample_building_id)

        data = Refiner(target_html).get_refined_data()
        building = Building(data)
        return building

    # Cralwer function
    def get_building_list(self, code: str) -> "json":
        url = self.building_list_url(code)
        response = self.get_request(url)
        return response.json()

    def get_building_detail_html(self, building_id: str) -> str:
        url = self.building_detail_url(building_id)
        response = self.get_request(url)
        return response.text

    # Target url information
    def building_list_url(self, code: str) -> str:
        url = f"{self.baseURL}/ajax/complexListByCortarNo?cortarNo={code}"
        return url

    def building_detail_url(self, building_id: str) -> str:
        url = f"{self.baseURL}/info/{building_id}?tradTpCd=A1:B1:B2&ajax=y"
        return url
