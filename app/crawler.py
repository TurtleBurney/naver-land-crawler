import re

from models.building import Building
from selenium.webdriver.common.by import By


def get_building_count(driver):
    items = driver.find_elements(By.CLASS_NAME, "result_item")
    return len(items)


def crawl_buildings(driver):  # crawl building으로 이름 변경
    building_list = []

    # TODO : naming problem... dong_household...
    building_name = driver.find_elements_by_class_name("heading")[7].text
    built_year = driver.find_elements_by_class_name("data")[5].text
    deal_count = driver.find_elements_by_class_name("txt_price")[0].text
    tnant_count = driver.find_elements_by_class_name("txt_price")[1].text
    rent_count = driver.find_elements_by_class_name("txt_price")[2].text
    land_address = driver.find_elements_by_class_name("p_address_place._addr").text
    road_address = driver.find_elements_by_class_name(
        "p_address_place._road_addr"
    ).text[8:]
    # 아래 변수들은 split 후 다른 변수에 담아 인스턴스에 할당
    category = driver.find_element_by_class_name(
        "label_detail.label_detail--positive"
    ).text[:-3]
    dong_hosehold_string = driver.find_elements_by_class_name("data")[2].text

    string_split = dong_hosehold_string.split()
    if len(string_split) == 1:
        total_dong_and_household = re.split("세대|동", dong_hosehold_string)
        total_dong = total_dong_and_household[1][1:]
        total_household = total_dong_and_household[0]
    else:
        total_dong = string_split[3][1:-3]
        total_household = string_split[:-6]

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
    building_list.append(building)
    return building_list


if __name__ == "__main__":
    get_building_count()


# 100세대(1동)
# 1,910세대(임대 326세대 포함, 총22동)
