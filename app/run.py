import time
import structlog
from app.crawler import get_target_buildings, crawl_building
from selenium.common.exceptions import WebDriverException
from app.client import NaverClient

logger = structlog.get_logger()


def run(scheduler):
    """
    scheduler와 함께 crawler 함수 호출
    """
    try:
        crawler()
    except WebDriverException as e:
        logger.error(f"Crawler is stopped by [{e}]")
    # scheduler.add_job(crawler, "cron", second="*/30", id="naver-crawler")


def crawler():
    """
    Selenium을 통해 url에서 javascript 활성화시키며 Building 정보 크롤링
    """
    try:
        logger.info(f' crawler :  1회 실행  {time.strftime("%H:%M:%S")}')

        Client = NaverClient()
        Client.click_main()

        ## SELECT SIGUNGU
        Client.click_address("first")
        Client.sleep(1)

        target_building_list = get_target_buildings(Client.driver)
        logger.info(f" crawler :  target_building_list 저장완료")

        for index in target_building_list:
            logger.info(f" crawler :  building[{index}] 크롤링 시작")

            Client.click("i_th_building_tag", index)  # i번째 건물 선택
            Client.click("REGION_SHOW_TAG")  # 지도로 보기 클릭
            Client.click("BUILDING_SHOW_TAG")  # 건물 정보 상세보기
            Client.sleep(3)

            building_list = crawl_building(Client.driver)

            # 전체 건물리스트로 재접근을 위해 주소탭 클릭
            Client.back(2)  # move back
            Client.click_address()
            Client.click("REGION_SHOW_TAG")  # 지도에서 보기 클릭

        logger.info(f" crawler :  building 크롤링 완료")
    except Exception as e:
        logger.info(f" crawler : crawler is stopped {e}")

    finally:
        Client.driver.quit()
        logger.info(f" crawler :  driver is closed")
