from crawler.base import BaseCrawler
from logger import init_logger
from object import Building, Refiner

logger = init_logger()


class BuildingCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.region_code = None

        logger.info("Crawler initated >> .... Crawl")

    def set_region(self, region_code: str) -> None:
        self.region_code = region_code

        logger.info(f"Region Setting >> Start Crawl {region_code}")

    def crawl(self) -> Building:
        # Building 여러개 가져와야함 지금 큰일남
        # TODO : sample이 아니라 반복문 돌며 가져와야 함

        # Step 1
        url = self.building_list_url(self.region_code)
        json_response = self.send_request(url).json()

        building_list = json_response
        sample_building = building_list["result"][0]
        sample_building_id = sample_building["hscpNo"]  # 110209

        # Step 2
        url = self.building_detail_url(sample_building_id)
        text_response = self.send_request(url).text

        data = Refiner(text_response).get_refined_data()
        building = Building(data, self.region_code, sample_building_id)

        buildings = list()
        buildings.append(building)

        return buildings

    # Target url information
    def building_list_url(self, code: str) -> str:
        url = f"{self.baseURL}/ajax/complexListByCortarNo?cortarNo={code}"
        return url

    def building_detail_url(self, building_id: str) -> str:
        url = f"{self.baseURL}/info/{building_id}?tradTpCd=A1:B1:B2&ajax=y"
        return url
