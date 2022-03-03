"""
naver crawler

"""
import json

from flask import app
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
    def get_building_list(self, code: str) -> json:
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

    def filter_building_detail(self, soup) -> None:
        building_name = soup.find("strong", "detail_complex_title").text
        total_household = soup.find_all("span", "detail_data_item")[0].text[:-2]
        lowest_floor = soup.find_all("span", "data")[1].text
        highest_floor = soup.find_all("span", "data")[1].text
        approval_date = soup.find_all("span", "detail_data_item")[2].text
        total_dong = soup.find_all("span", "detail_data_item")[1].text
        # number_address = 
        # road_address = 
        total_deal = soup.find_all("em", "txt_price")[0].text
        total_jeonse = soup.find_all("em", "txt_price")[1].text
        total_wolse = soup.find_all("em", "txt_price")[2].text
        print(building_name, total_household, lowest_floor, highest_floor, approval_date, total_deal, sep="\n")


if __name__ == "__main__":
    crawler = NaverLandCrawler()
    target_html = crawler.get_building_detail_html("110209")
    soup = BeautifulSoup(target_html, "html.parser")
    crawler.filter_building_detail(soup)

    file = open("sample.html", "w", encoding="UTF-8")
    file.write(target_html)
    file.close()
