from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import CHROME_DRIVER_PATH
from model.buildings import Building

# 데이터 클래스 설정
general_data = []
specific_data = []

url = "https://m.land.naver.com/"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(url)  # 연다

apt_btn = driver.find_element_by_class_name(
    "home_main_button.first_line._rletTypeBtn._innerLink"
)
apt_btn.click()

# 주소 변경 탭 활성화
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='mapSearch']/div[2]/div[3]/div/div[2]/div[1]/a")
    )
).click()
# 주소 입력(시, 구, 동)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[1]/a",
        )
    )
).click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/a",
        )
    )
).click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[3]/div[2]/div/div/table/tbody/tr[3]/td[2]/a",
        )
    )
).click()
driver.implicitly_wait(20)

ahyun = []
# 북아현동 아파트, 오피스텔 개괄적인 정보 저장
for i, item in enumerate(driver.find_elements(By.CLASS_NAME, "result_item")):
    info = item.text.split()
    ahyun.append(info)

# 이름, 종류(오피스텔, 아파트) 추출(수정해야함)
for i in range(len(ahyun)):
    type_mm = ahyun[i][1].split("매매")
    js_ws_tmp = ahyun[i][2].split("전세")
    js_ws = js_ws_tmp[1].split("월세")
    b = Building(
        building_name=ahyun[i][0],
        building_type=type_mm[0],
        # contract_type=,
        trading_num=type_mm[1],
        tenant_num=js_ws[0],
        wolse_num=js_ws[1],
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

# 아파트 정보 추출
# 매물 수가 0보다 크면 서치해라
"""
e편한 오피스텔 : //*[@id="mapSearch"]/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[1]/a
e편한 아파트   : //*[@id="mapSearch"]/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[2]/a
li[x] (x = 1, 2, ..., len(ahyun))
"""
# for x in range(len(ahyun)):
#     if (int(ahyun[x][1]) > 0): # 매매 매물이 있을 때
#         WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[{0}]/a".format(x + 1)))).click()
#         # 지도로 보기 클릭
#         WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mapSearch']/div[2]/div[1]/section/div[2]/a"))).click()
#         # 상세 정보 보기 클릭
#         WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a"))).click()
#         # 매매로 이동
#         WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_basic_content_cd']/div[1]/div[4]/ul/li[1]/a"))).click()
#         driver.implicitly_wait(50)

#         # 각 매물에 접근
#         # for i in range(int(ahyun[x][1])):
#         building_name = driver.find_elements(By.CLASS_NAME, 'title_place')
#         building_dong = driver.find_elements(By.CLASS_NAME, 'title_building')
#         # 새로운 데이터타입 만드는게 우선(그 다음 각 아파트에 대한 매물 정보 저장)
#         print(building_dong[0].text)
#         # driver.quit()
