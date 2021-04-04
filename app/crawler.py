import re
import time
import structlog
from models.building import Building
from app.client.db import DBClient
from app.client.web import NaverClient
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import ProtocolError

logger = structlog.get_logger()


class NaverCrawler(object):
    def __init__(self, config):
        super().__init__()

        #: Config Setting
        self.config = config

        #: Client Setting
        self.naver_client = NaverClient(self.config)
        self.db_Client = DBClient(self.config)

    def run(self, mode="DEBUG"):
        client = self.naver_client
        try:
            building_list = self.crawl_buildings_info(client)
            print(building_list)

        except KeyboardInterrupt:
            logger.warn("Keyboard Interrunption !")
            raise
        else:
            client.quit()

        finally:
            logger.info(f" crawler :  driver is closed")

    def crawl_buildings_info(self, client):
        client.click_main()
        client.click_address("first")
        client.sleep(1)

        quantities = client.crawl_quantities()
        target_building_list = self.get_target_buildings(quantities)

        building_list = list()
        for index in target_building_list:
            logger.info(f" crawler :  building[{index}] 크롤링 시작")

            client.click("i_th_building_tag", index)  # i번째 건물 선택
            client.click("VIEW_ON_MAP_TAG")  # 지도로 보기 클릭
            client.click("BUILDING_LIST_SHOW_TAG")  # 건물 정보 상세보기
            client.sleep(3)

            building_info = self.crawl_building()
            building_list.append(building_info)

            # 전체 건물리스트로 재접근을 위해 주소탭 클릭
            client.back(2)  # move back
            client.click_address()
            client.click("VIEW_ON_MAP_TAG")  # 지도에서 보기 클릭

        logger.info(f" crawler :  building 크롤링 완료")
        return building_list

    def get_target_buildings(self, quantities):
        """
        해당 동의 아파트, 오피스텔 list를 통해
        매물(매매, 전세, 월세)이 존재하는 건물 index의 배열을 return하는 함수
        """
        target_building_list = []
        property_count = 0
        del quantities[3]  # 단기임대 생성에 따른 임시방편

        for index, building in enumerate(quantities):
            property_count = property_count + int(building.text)
            if (index + 1) % 3 == 0:
                if property_count > 0:
                    target_building_list.append(index // 3)
                property_count = 0

        return target_building_list

    def crawl_building(self):
        """
        Building class를 생성할 data crawling
        """
        driver = self.naver_client.driver
        # Building Class의 속성
        building_name = driver.find_elements_by_class_name("heading")[7].text
        deal_count = driver.find_elements_by_class_name("txt_price")[0].text
        tnant_count = driver.find_elements_by_class_name("txt_price")[1].text
        rent_count = driver.find_elements_by_class_name("txt_price")[2].text
        land_address = driver.find_element_by_class_name("p_address_place._addr").text
        road_address = driver.find_element_by_class_name(
            "p_address_road._road_addr"
        ).text[8:]
        category = driver.find_element_by_class_name(
            "label_detail.label_detail--positive"
        ).text[:-3]

        try:
            # 최근에 매매된 기록이 있는지 판단 (class name이 data인 배열에 '최근 거래가'요소 추가로 인덱스 밀림)
            whether_deal_recently = driver.find_element_by_class_name("date")

            # 최근에 매매된 기록이 있을 때
            household_info = driver.find_elements_by_class_name("data")[3].text
            built_year = driver.find_elements_by_class_name("data")[6].text
        except:
            # 최근에 매매된 기록이 없을 때
            household_info = driver.find_elements_by_class_name("data")[2].text
            built_year = driver.find_elements_by_class_name("data")[5].text

        # 크롤링 된 내용 가공
        total_dong, total_household = self.split_household_info(household_info)

        building = Building(
            name=building_name,
            category=category,
            deal_count=deal_count,
            tnant_count=tnant_count,
            rent_count=rent_count,
            built_year=built_year,
            total_dong=total_dong,
            total_household=total_household,
            land_address=land_address,
            road_address=road_address,
        )
        return building

    def split_household_info(self, household_info):
        """
        크롤링으로 data 받아올 시, total_dong, total_household 변수 값이 하나의 text로 담겨와
        household_info를 split하여 total_dong, total_household 각각에 할당
        """
        household_info_split = household_info.split()
        if len(household_info_split) == 1:
            total_dong_and_household = re.split("세대|동", household_info)
            total_dong = total_dong_and_household[1][1:]
            total_household = total_dong_and_household[0]
        else:
            total_dong = household_info_split[3][1:-2]
            total_household = household_info_split[0][:-5]
        return total_dong, total_household
