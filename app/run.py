import time
import structlog
from app.client import move_to_page, move_to_each_page, move_back
from app.crawler import crawl_general_data, crawl_specific_data


logger = structlog.get_logger()


def run(scheduler):
    crawler()
    # scheduler.add_job(crawler, "cron", second="*/30", id="naver-crawler")


def crawler():
    logger.info(f' crawler :  1회 실행  {time.strftime("%H:%M:%S")}')
    url = "https://m.land.naver.com/"
    driver = move_to_page(url)
    driver, general_data = crawl_general_data(driver)
    for i in range(len(general_data)):
        driver = move_to_each_page(driver, i)
        driver = crawl_specific_data(driver, general_data, i)
        driver = move_back(driver)
