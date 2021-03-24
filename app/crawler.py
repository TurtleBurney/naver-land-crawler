import re

from models.building import Building
from selenium.webdriver.common.by import By
from app.client import click_javascript_void

def crawl_general_data(driver):
    building_in_dong = []

    # 북아현동 아파트, 오피스텔 개괄적인 정보 저장
    for i, item in enumerate(driver.find_elements(By.CLASS_NAME, "result_item")):
        info = item.text.split()
        building_in_dong.append(info)

    general_data = []

    for i in range(len(building_in_dong)):
        type_trading = building_in_dong[i][1].split("매매")
        tenant_wolse = re.split("전세|월세", building_in_dong[i][2])[1:]
        general_data.append(
            Building(
                name=building_in_dong[i][0],
                category=type_trading[0],
                deal_count=type_trading[1],
                tnant_count=tenant_wolse[0],
                rent_count=tenant_wolse[1],
            )
        )
        if general_data[i].deal_count == 0:
            general_data[i].deal_count = 0
        if general_data[i].tnant_count == 0:
            general_data[i].tnant_count = 0
        if general_data[i].rent_count == 0:
            general_data[i].rent_count = 0

    return driver, general_data

def crawl_specific_data(driver, general_data, i):
    built_year = driver.find_element_by_xpath("//*[@id='_basic_content_cd']/article[1]/div[2]/div/div[2]/div[2]/span[2]").text
    raw_dong_and_hosehold = driver.find_element_by_xpath("//*[@id='_basic_content_cd']/article[1]/div[2]/div/div[1]/div[1]/span[2]").text
    land_address = driver.find_element_by_xpath("//*[@id='_basic_content_cd']/article[4]/div[2]/p[1]").text
    road_address = driver.find_element_by_xpath("//*[@id='_basic_content_cd']/article[4]/div[2]/p[2]").text
    # 예외 발생(1,910세대(임대 326세대 포함, 총22동)) << 이의 경우 out of range 오류 발생
    total_dong_and_household = re.split("세대|동", raw_dong_and_hosehold) # 괄호 지우기는 방법이 이상적이지만 실패

    general_data[i].built_year = built_year
    general_data[i].total_dong = total_dong_and_household[1][1:]
    general_data[i].total_household = total_dong_and_household[0]
    general_data[i].land_address = land_address
    general_data[i].road_address = road_address[8:]

    return driver
    
if __name__ == "__main__":
    crawl_general_data()
