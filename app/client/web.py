import os
import time
import structlog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logger = structlog.get_logger()



# 주소 변경 탭 활성화
SEARCH_ID = "//*[@id='mapSearch']"
OPEN_ADDRESS_TAB_TAG = f"{SEARCH_ID}/div[2]/div[3]/div/div[2]/div[1]/a"
REOPEN_ADDRESS_TAB_TAG = f"{SEARCH_ID}/div[2]/div[3]/div/div[2]/div[2]/a"

## SELECT SIGUNGU
REGION_AREA_TAG = f"{SEARCH_ID}/div[2]/div[1]/section/div[1]/"
REGION_SHOW_TAG = f"{SEARCH_ID}/div[2]/div[1]/section/div[2]/a"
BUILDING_SHOW_TAG = "//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a"
TABLE_TAG = "div[2]/div/div/table/tbody/"

step3_bukahyun_tag = f"{REGION_AREA_TAG}div[3]/{TABLE_TAG}tr[3]/td[2]/a"
i_th_building_tag = f"{REGION_AREA_TAG}div[4]/div/div[2]/div/ul/"


class NaverClient(object):
    """
    Naver
    """

    def __init__(self, config=None):
        super().__init__()

        self.url = "https://m.land.naver.com/map/37.558332:126.956197:18:/APT:JGC/A1:B1:B2#regionStep3"
        self.driver = self.init_driver()

    def init_driver(self):

        # Webdriver를 통해 해당 url의 chrome창 활성화
        driver = webdriver.Chrome(os.path.join("libs", "chromedriver.exe"))
        driver.get(self.url)
        logger.info(f" crawler :  chrome창 활성화 완료")

        return driver

    def click(self, tag, index=0):
        logger.info(f" click : {tag}")

        tag_list = {
            "REGION_SHOW_TAG": REGION_SHOW_TAG,
            "BUILDING_SHOW_TAG": BUILDING_SHOW_TAG,
            "i_th_building_tag": f"{i_th_building_tag}li[{(index+1)}]/a",
        }

        if tag in tag_list:
            tag = tag_list[tag]

        WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, f"{tag}"))
        ).click()

    def click_address(self, flag=None):
        # 주소탭 활성화
        if flag == "first":
            self.click(OPEN_ADDRESS_TAB_TAG)
        else:
            self.click(REOPEN_ADDRESS_TAB_TAG)  

        self.click(step3_bukahyun_tag)  # 읍/면/동 선택에서 '북아현동' 선택

    def back(self, iteration):
        for i in range(iteration):
            self.driver.back()

    def sleep(self, ms):
        time.sleep(ms)

    def quit(self):
        self.driver.quit()


def click(driver, tag):
    # javascript tag를 클릭하기 위한 함수
    WebDriverWait(driver, 500).until(
        EC.element_to_be_clickable((By.XPATH, f"{tag}"))
    ).click()


if __name__ == "__main__":
    init_driver()
