import os
import time
import structlog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logger = structlog.get_logger()


MAIN_APT_BUTTON_TAG = "home_main_button.first_line._rletTypeBtn._innerLink"
# 주소 변경 탭 활성화
SEARCH_ID = "//*[@id='mapSearch']"
OPEN_ADDRESS_TAB_TAG = f"{SEARCH_ID}/div[2]/div[3]/div/div[2]/div[1]/a"
REOPEN_ADDRESS_TAB_TAG = f"{SEARCH_ID}/div[2]/div[3]/div/div[2]/div[2]/a"

## SELECT SIGUNGU
REGION_AREA_TAG = f"{SEARCH_ID}/div[2]/div[1]/section/div[1]/"
VIEW_ON_MAP_TAG = f"{SEARCH_ID}/div[2]/div[1]/section/div[2]/a"
BUILDING_LIST_SHOW_TAG = "//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a"
TABLE_TAG = "div[2]/div/div/table/tbody/"

step0_address_tag = f"{REGION_AREA_TAG}div[3]/div[1]/div/a[1]"
step1_seoul_tag = f"{REGION_AREA_TAG}div[1]/{TABLE_TAG}tr[1]/td[1]/a"
step2_sudamoon_tag = f"{REGION_AREA_TAG}div[2]/{TABLE_TAG}tr[5]/td[2]/a"
step3_bukahyun_tag = f"{REGION_AREA_TAG}div[3]/{TABLE_TAG}tr[3]/td[2]/a"
i_th_building_tag = f"{REGION_AREA_TAG}div[4]/div/div[2]/div/ul/"


class NaverClient(object):
    """
    Naver
    """

    def __init__(self, config=None):
        super().__init__()

        self.url = "https://m.land.naver.com/"
        self.driver = self.init_driver()

    def init_driver(self):
        # Webdriver를 통해 해당 url의 chrome창 활성화
        try:
            logger.info(f" naver-client : init driver")

            driver = webdriver.Chrome(os.path.join("libs", "chromedriver.exe"))
            driver.get(self.url)
            return driver

        except:
            logger.warn(" naver-clinet : driver connection fail")
            return None

    def click(self, tag, index=0):
        # javascrip:void(0)를 이용해 창 변화
        # logger.info(f" click : {tag}")

        tag_list = {
            "VIEW_ON_MAP_TAG": VIEW_ON_MAP_TAG,
            "BUILDING_LIST_SHOW_TAG": BUILDING_LIST_SHOW_TAG,
            "i_th_building_tag": f"{i_th_building_tag}li[{(index+1)}]/a",
        }

        if tag in tag_list:
            tag = tag_list[tag]

        WebDriverWait(self.driver, 200).until(
            EC.element_to_be_clickable((By.XPATH, f"{tag}"))
        ).click()

    def click_main(self):
        self.driver.find_element_by_class_name(MAIN_APT_BUTTON_TAG).click()

    def click_address(self, flag=None):
        # 주소탭 활성화
        if flag == "first":
            self.click(OPEN_ADDRESS_TAB_TAG)
            self.click(step1_seoul_tag)  # 시/도 선택에서 '서울시' 선택
            self.click(step2_sudamoon_tag)  # 시/군/구 선택에서 '서대문구' 선택
        else:
            self.click(REOPEN_ADDRESS_TAB_TAG)

        self.click(step3_bukahyun_tag)  # 읍/면/동 선택에서 '북아현동' 선택

    def back(self, iteration):
        for i in range(iteration):
            self.driver.back()

    def sleep(self, s):
        time.sleep(s)

    def quit(self):
        self.driver.quit()

    def crawl_quantities(self):
        quantities = self.driver.find_elements_by_class_name("quantity")
        return quantities


if __name__ == "__main__":
    init_driver()
