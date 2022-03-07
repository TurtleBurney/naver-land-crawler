"""
naver crawler

"""
import requests
import utils
from bs4 import BeautifulSoup


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

    def filter_building_info_tags(self, soup):
        tags = {}
        tags["prices"] = soup.find_all("em", "txt_price")
        tags["floors"] = soup.find_all("span", "data")
        tags["title"] = soup.find("strong", "detail_complex_title")
        tags["details"] = soup.find_all("span", "detail_data_item")
        tags["addresses"] = soup.find_all('script', type='text/javascript')
        return tags

    def refine_address_data(self, tags):
        address = {}
        lump_address = tags["addresses"][2].text.split("addr")[1].split("realPriceInfoYn")[0]
        lump_splitted = lump_address.split(",")
        number_ver = lump_splitted[0][4:-2]
        lump_road = lump_splitted[-2].split("'")
        road_ver = lump_road[1]
        address["number"] = number_ver
        address["road"] = road_ver
        return address

    def refine_floor_data(self, tags):
        floor = {}
        floor_tag = tags["floors"][1].text
        splitted_floor = floor_tag.split("/")
        floor["low"] = splitted_floor[0]
        floor["high"] = splitted_floor[1][:-1]
        return floor

    def filter_building_detail(self, tags) -> None:
        floors = self.refine_floor_data(tags)
        address = self.refine_address_data(tags)
        building_name = tags["title"].text
        total_household = tags["details"][0].text[:-2]
        lowest_floor = floors["low"]
        highest_floor = floors["high"]
        approval_date = tags["details"][2].text
        total_dong = tags["details"][1].text
        number_address = address["number"]
        road_address = address["road"]
        total_deal = tags["prices"][0].text
        total_jeonse = tags["prices"][1].text
        total_wolse = tags["prices"][2].text
        print(building_name, total_household, lowest_floor, highest_floor, approval_date, total_deal, number_address, road_address, sep="\n")


if __name__ == "__main__":
    crawler = NaverLandCrawler()
    building_list = crawler.get_building_list("1141011000")
    # 반복문으로 building_id마다 크롤링 예정
    target_html = crawler.get_building_detail_html("110209")
    soup = BeautifulSoup(target_html, "html.parser")
    tags = crawler.filter_building_info_tags(soup)
    crawler.filter_building_detail(tags)
