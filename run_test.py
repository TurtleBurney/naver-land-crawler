from app.client import move_to_page
from app.crawler import crawl_general_data

url = "https://m.land.naver.com/"

driver = move_to_page(url)
crawl_general_data(driver)
