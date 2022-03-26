"""
naver crawler

"""
import requests

import utils
from object.building import Building
from object.refiner import Refiner


class NaverLandCrawler:
    """
    Naver Land Cralwer

    """

    def __init__(self) -> None:
        self.baseURL = "https://m.land.naver.com/complex"

    def run(self):
        # TODO : DB에서 region_code 읽어오기
        sample_region_code = "1141011000"
        building_list = self.get_building_list(sample_region_code)

        # TODO : 반복문으로 building_id마다 크롤링
        sample_building = building_list["result"][0]
        sample_building_id = sample_building["hscpNo"]  # 110209
        target_html = self.get_building_detail_html(sample_building_id)

        # TODO : Building 정보 DB에 넣기
        data = Refiner(target_html).get_refined_data()
        building = Building(data)

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

    # API request
    def get_request(self, url: str) -> requests.Response:
        header = utils.setup_header()
        response = requests.get(url, headers=header, allow_redirects=False)
        return response


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
