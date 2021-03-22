import re

from model.buildings import Building
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
                building_name=building_in_dong[i][0],
                building_type=type_trading[0],
                trading_num=type_trading[1],
                tenant_num=tenant_wolse[0],
                wolse_num=tenant_wolse[1],
            )
        )
    return driver


def crawl_specific_data(driver):
    # if (매물s[x]매물 수가 0보다 크다면):
    WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[{0}]/a".format(
                        x + 1
                    ),
                )
            )
        ).click()

    # 지도로 보기 클릭
    WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='mapSearch']/div[2]/div[1]/section/div[2]/a")
        )
    ).click()
    # 상세 정보 보기 클릭
    WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a")
        )
    ).click()
    


if __name__ == "__main__":
    crawl_general_data()
