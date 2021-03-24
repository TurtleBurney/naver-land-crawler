import re

from models.building import Building
from selenium.webdriver.common.by import By


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

        print(type_trading)
        print(tenant_wolse)
        
    print(general_data[0])
    return driver, general_data

# git 꼬임

# def crawl_specific_data(driver, general_data):
#     # if (general_data): 
#     WebDriverWait(driver, 50).until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[{0}]/a".format(
#                         x + 1
#                     ),
#                 )
#             )
#         ).click()

#     # 지도로 보기 클릭
#     WebDriverWait(driver, 50).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//*[@id='mapSearch']/div[2]/div[1]/section/div[2]/a")
#         )
#     ).click()
#     # 상세 정보 보기 클릭
#     WebDriverWait(driver, 50).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a")
#         )
#     ).click()
>>>>>>> 6431ba421ac941ac189960fc42996de4c8c0093f
    


if __name__ == "__main__":
    crawl_general_data()
