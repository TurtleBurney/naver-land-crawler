import re

from models.building import Building
from selenium.webdriver.common.by import By


def get_building_count(driver):
    """
    해당 동의 아파트, 오피스텔 list를 통해 2개의 변수를 return하는 함수
    1. 해당 동의 아파트, 오피스텔 건물 수
    2. 매물(매매, 전세, 월세)이 존재하는 건물 index의 배열
    """
    quantities = driver.find_elements_by_class_name("quantity")
    crawlable_list = []
    count, property_count = 0, 0
    for index, building in enumerate(quantities):
        if count < 2:
            property_count = property_count + int(building.text)
            count += 1
        else:
            property_count = property_count + int(building.text)
            crawlable = True if property_count > 0 else False
            if crawlable is True:
                crawlable_list.append(index // 3)
            count, property_count = 0, 0
    return crawlable_list


def crawl_buildings(driver):
    # Building class를 생성할 data crawling
    building_list = []

    # Building Class의 속성 크롤링
    building_name = driver.find_elements_by_class_name("heading")[7].text
    deal_count = driver.find_elements_by_class_name("txt_price")[0].text
    tnant_count = driver.find_elements_by_class_name("txt_price")[1].text
    rent_count = driver.find_elements_by_class_name("txt_price")[2].text
    land_address = driver.find_element_by_class_name("p_address_place._addr").text
    road_address = driver.find_element_by_class_name("p_address_road._road_addr").text[8:]
    category = driver.find_element_by_class_name("label_detail.label_detail--positive").text[:-3]
    
    """
    최근에 매매된 기록이 있는지 판단
    최근에 매매된 기록이 있다 -> class name이 data인 배열에 '최근 거래가'요소 추가로 인덱스 밀림
    """
    try:
        whether_deal_recently = driver.find_element_by_class_name("date")
        household_info = driver.find_elements_by_class_name("data")[3].text
        built_year = driver.find_elements_by_class_name("data")[6].text
    except:
        household_info = driver.find_elements_by_class_name("data")[2].text
        built_year = driver.find_elements_by_class_name("data")[5].text
    

    # 크롤링 된 내용 가공
    household_info_split = household_info.split()
    if len(household_info_split) == 1:
        total_dong_and_household = re.split("세대|동", household_info)
        total_dong = total_dong_and_household[1][1:]
        total_household = total_dong_and_household[0]
    else:
        total_dong = household_info_split[3][1:-2]
        total_household = household_info_split[0][:-5]

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
