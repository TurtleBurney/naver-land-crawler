"""
naver crawler

"""
import requests

import utils

from object.refiner import Refiner
from object.building import Building


class NaverLandCrawler:
    """
    Naver Land Cralwer

    """

    def __init__(self) -> None:
        self.baseURL = "https://m.land.naver.com/complex"

    # Cralwer function
    def get_building_list(self, code: str) -> "json":
        url = self.building_list_url(code)
        response = self.get_request(url)
        return response.json()

    def get_building_detail_html(self, building_id: str) -> str:
        url = self.building_detail_url(building_id)
        response = self.get_request(url)
        return response.text

    # API Request
    def get_request(self, url: str) -> requests.Response:
        header = utils.setup_header()
        response = requests.get(url, headers=header, allow_redirects=False)
        return response

    # URL
    def building_list_url(self, code: str) -> str:
        url = f"{self.baseURL}/ajax/complexListByCortarNo?cortarNo={code}"
        return url

    def building_detail_url(self, building_id: str) -> str:
        url = f"{self.baseURL}/info/{building_id}?tradTpCd=A1:B1:B2&ajax=y"
        return url


if __name__ == "__main__":
    crawler = NaverLandCrawler()
    building_list = crawler.get_building_list("1141011000")
    # 반복문으로 building_id마다 크롤링 예정
    target_html = crawler.get_building_detail_html("110209")
    data = Refiner(target_html).get_refined_data()
    building = Building(data)
