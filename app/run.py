import time
import structlog
from app.client import move_to_page
from app.crawler import crawl_general_data


logger = structlog.get_logger()


def run(scheduler):
    crawler()
    # scheduler.add_job(crawler, "cron", second="*/30", id="naver-crawler")


def crawler():
    logger.info(f' crawler :  1회 실행  {time.strftime("%H:%M:%S")}')
    url = "https://m.land.naver.com/"
    driver = move_to_page(url)
    crawl_general_data(driver)
