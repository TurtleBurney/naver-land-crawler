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
        # Step 1
        url = self.building_list_url(self.region_code)
        json_response = self.send_request(url).json()

        building_list = json_response["result"]
        buildings = list()

        # Step 2
        for building in building_list:
            building_id = building["hscpNo"]

            url = self.building_detail_url(building_id)
            text_response = self.send_request(url).text

            data = Refiner(text_response).get_refined_data()
            building = Building(data, self.region_code, building_id)

            buildings.append(building)
        return buildings

    # Target url information
    def building_list_url(self, code: str) -> str:
        url = f"{self.baseURL}/ajax/complexListByCortarNo?cortarNo={code}"
        return url

    def building_detail_url(self, building_id: str) -> str:
        url = f"{self.baseURL}/info/{building_id}?tradTpCd=A1:B1:B2&ajax=y"
        return url
