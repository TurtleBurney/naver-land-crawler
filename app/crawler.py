import re

from model.buildings import Building
from selenium.webdriver.common.by import By


def crawl_general_data(driver):
    ahyun = []

    # 북아현동 아파트, 오피스텔 개괄적인 정보 저장
    for i, item in enumerate(driver.find_elements(By.CLASS_NAME, "result_item")):
        info = item.text.split()
        ahyun.append(info)

    general_data = []

    for i in range(len(ahyun)):
        type_trading = ahyun[i][1].split("매매")
        tenant_wolse = re.split("전세|월세", ahyun[i][2])[1:]
        b = Building(
            building_name=ahyun[i][0],
            building_type=type_trading[0],
            # contract_type=,
            trading_num=type_trading[1],
            tenant_num=tenant_wolse[0],
            wolse_num=tenant_wolse[1],
            # building_dong=,
            # exclusive_area=,
            # shared_area=,
            # target_floor=,
            # max_floor=,
            # window_side=,
            # trading_price_min=,
            # trading_price_max=
        )
        print(b)
        general_data.append(b)


if __name__ == "__main__":
    crawl_general_data()
