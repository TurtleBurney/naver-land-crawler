import re

from models.building import Building
from selenium.webdriver.common.by import By


def crawl_buildings(driver):
    # 북아현동 아파트, 오피스텔 개괄적인 정보 저장
    building_list = []
    items = driver.find_elements(By.CLASS_NAME, "result_item")
    for item in items:
        building_info = item.text.split()
        building_name = building_info[0]

        # TODO : elements tag로 찾기
        category = building_info[1].split("매매")[0]
        deal_count = building_info[1].split("매매")[1]
        tnant_count = re.split("전세|월세", building_info[2])[1]
        rent_count = re.split("전세|월세", building_info[2])[2]

        building = Building(
            name=building_name,
            category=category,
            deal_count=deal_count,
            tnant_count=tnant_count,
            rent_count=rent_count,
        )
        building_list.append(building)
    
    return building_list


def crawl_households(driver, building):
    # TODO : naming problem... dong_household...
    ID_TAG = "//*[@id='_basic_content_cd']/"

    BUILDING_INFO_TAG = f"{ID_TAG}article[1]/div[2]/div/"

    dong_household_tag = f"{BUILDING_INFO_TAG}div[1]/div[1]/span[2]"
    built_year_tag = f"{BUILDING_INFO_TAG}div[2]/div[2]/span[2]"

    built_year = driver.find_element_by_xpath(built_year_tag).text
    dong_hosehold_string = driver.find_element_by_xpath(dong_household_tag).text
    # 예외 발생(1,910세대(임대 326세대 포함, 총22동)) << 이의 경우 out of range 오류 발생
    dong_household = re.split("세대|동", dong_hosehold_string)

    land_address = driver.find_element_by_xpath(ID_TAG + "article[4]/div[2]/p[1]").text
    road_address = driver.find_element_by_xpath(ID_TAG + "article[4]/div[2]/p[2]").text

    building.built_year = built_year
    building.total_household = dong_household[0]

    building.land_address = land_address
    building.road_address = road_address[8:]

    # TODO : 조건문으로 예외처리하기
    building.total_dong = dong_household[1][1:]


if __name__ == "__main__":
    crawl_buildings()


# 100세대(1동)
# 1,910세대(임대 326세대 포함, 총22동)
