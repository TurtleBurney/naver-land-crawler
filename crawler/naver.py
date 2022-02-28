"""
naver crawler

"""
import json
import utils
import requests
from bs4 import BeautifulSoup


class NaverLandCrawler:
    """
    Naver Land Cralwer

    """

    def __init__(self) -> None:
        self.baseURL = "https://m.land.naver.com/complex"

    # Cralwer function
    def get_building_json(self, code) -> json:
        url = self.building_list_url(code)
        response = self.get_request(url)
        return response.json()

    def get_building_detail_text(self, hscpNo) -> str:
        url = self.building_list_url(hscpNo)
        response = self.get_request(url)
        return response.text

    # API Request
    def get_request(self, url: str) -> requests.Response:
        header = utils.setup_header()
        response = requests.get(url, headers=header, allow_redirects=False)
        return response

    # URL
    def building_list_url(self, code) -> str:
        url = f"{self.baseURL}/ajax/complexListByCortarNo?cortarNo={code}"
        return url

    def building_detail_url(self, hscpNo) -> str:
        url = f"{self.baseURL}/info/{hscpNo}?tradTpCd=A1:B1:B2&ajax=y"
        return url

    # 건물 목록 + 건물 detail 정보 필요
    def filter_building_info(self, basic_info) -> None:
        building_info = basic_info["result"][0]

        building_name = building_info["hscpNm"]
        building_type = building_info["hscpTypeNm"]
        total_deal = building_info["dealCnt"]
        total_jeonse = building_info["leaseCnt"]
        total_wolse = building_info["rentCnt"]


if __name__ == "__main__":
    crawler = NaverLandCrawler()
    target_html = crawler.get_building_detail_text(110209)
    soup = BeautifulSoup(target_html, "html.parser")

    file = open("sample.html", "w", encoding="UTF-8")
    file.write(target_html)
    file.close()

    # 선택의 시간 두둥
    # 파라미터가 많은 복잡한 url VS html에서 태그찾기
    # https://m.land.naver.com/cluster/ajax/complexList?itemId=110209&mapKey=&lgeo=21221003332101&rletTpCd=OBYG:ABYG:OPST:APT:JGC&tradTpCd=A1:B1:B2&z=18&lat=37.558609&lon=126.951802&btm=37.5566167&lft=126.9496884&top=37.5606013&rgt=126.9539156&isOnlyIsale=false
