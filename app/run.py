import time
import structlog
from app.client import init_driver, click_void
from app.crawler import crawl_buildings, crawl_households


logger = structlog.get_logger()


def run(scheduler):
    crawler()
    # scheduler.add_job(crawler, "cron", second="*/30", id="naver-crawler")


def crawler():
    logger.info(f' crawler :  1회 실행  {time.strftime("%H:%M:%S")}')
    url = "https://m.land.naver.com/"

    driver = init_driver(url)

    MAIN_APT_BUTTON_TAG = "home_main_button.first_line._rletTypeBtn._innerLink"
    apt_btn = driver.find_element_by_class_name(MAIN_APT_BUTTON_TAG)
    apt_btn.click()

    # 주소 변경 탭 활성화
    SEARCH_ID = "//*[@id='mapSearch']"
    OPEN_ADDRESS_TAB_TAG = f"{SEARCH_ID}/div[2]/div[3]/div/div[2]/div[1]/a"
    REOPEN_ADDRESS_TAB_TAG = f"{SEARCH_ID}/div[2]/div[3]/div/div[2]/div[2]/a"

    ## SELECT SIGUNGU
    REGION_AREA_TAG = f"{SEARCH_ID}/div[2]/div[1]/section/div[1]/"
    REGION_SHOW_TAG = f"{SEARCH_ID}/div[2]/div[1]/section/div[2]/a"
    BUILDING_SHOW_TAG = "//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a"
    TABLE_TAG = "div[2]/div/div/table/tbody/"

    step0_address_tag = f"{REGION_AREA_TAG}div[3]/div[1]/div/a[1]"
    step1_seoul_tag = f"{REGION_AREA_TAG}div[1]/{TABLE_TAG}tr[1]/td[1]/a"
    step2_sudamoon_tag = f"{REGION_AREA_TAG}div[2]/{TABLE_TAG}tr[5]/td[2]/a"
    step3_bukahyun_tag = f"{REGION_AREA_TAG}div[3]/{TABLE_TAG}tr[3]/td[2]/a"

    click_void(driver, OPEN_ADDRESS_TAB_TAG)
    click_void(driver, step1_seoul_tag)  # 시/도 선택에서 '서울시' 선택
    click_void(driver, step2_sudamoon_tag)  # 시/군/구 선택에서 '서대문구' 선택
    click_void(driver, step3_bukahyun_tag)  # 읍/면/동 선택에서 '북아현동' 선택
    driver.implicitly_wait(20)
    ##

    building_list = crawl_buildings(driver)
    for i, building in enumerate(building_list):
        i_th_building_tag = f"{REGION_AREA_TAG}div[4]/div/div[2]/div/ul/li[{(i+1)}]/a"
        click_void(driver, i_th_building_tag)  # i번째 건물 선택
        click_void(driver, REGION_SHOW_TAG)  # 지도로 보기 클릭
        click_void(driver, BUILDING_SHOW_TAG)  # 건물 정보 상세보기

        crawl_households(driver, building)
        # move back
        driver.back()
        driver.back()
        # 전체 건물리스트로 재접근을 위해 주소탭 클릭
        click_void(driver, REOPEN_ADDRESS_TAB_TAG)  # 여기서 오류 발생중
        click_void(driver, step0_address_tag)  # 주소탭 초기화

        click_void(driver, step1_seoul_tag)  # 시/도 선택에서 '서울시' 선택
        click_void(driver, step2_sudamoon_tag)  # 시/군/구 선택에서 '서대문구' 선택
        click_void(driver, step3_bukahyun_tag)  # 읍/면/동 선택에서 '북아현동' 선택
        click_void(driver, REGION_SHOW_TAG)  # 지도에서 보기 클릭
