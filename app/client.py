import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def click_void(xpath, driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"{xpath}"))
    ).click()


def select_sigungu(driver):
    # 주소 입력(시, 구, 동)
    BASE_TAG = "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/"
    # 시/도 선택에서 '서울시' 선택
    click_void(BASE_TAG + "div[1]/div[2]/div/div/table/tbody/tr[1]/td[1]/a", driver)
    # 시/군/구 선택에서 '서대문구' 선택
    click_void(BASE_TAG + "div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/a", driver)
    # 읍/면/동 선택에서 '북아현동' 선택
    click_void(BASE_TAG + "div[3]/div[2]/div/div/table/tbody/tr[3]/td[2]/a", driver)
    driver.implicitly_wait(20)
    return driver


def move_to_page(url):
    driver = webdriver.Chrome(os.path.join("libs", "chromedriver.exe"))
    driver.get(url)

    apt_btn = driver.find_element_by_class_name(
        "home_main_button.first_line._rletTypeBtn._innerLink"
    )
    apt_btn.click()
    # 주소 변경 탭 활성화
    click_void("//*[@id='mapSearch']/div[2]/div[3]/div/div[2]/div[1]/a", driver)
    select_sigungu(driver)
    return driver


def move_to_each_page(driver, i):
    # i번째 건물 선택
    click_void(
        f"//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[{(i+1)}]/a",
        driver,
    )
    # 지도로 보기 클릭
    click_void("//*[@id='mapSearch']/div[2]/div[1]/section/div[2]/a", driver)
    # 건물 정보 상세보기
    click_void("//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a", driver)
    return driver


def move_back(driver):
    driver.back()
    driver.back()

    BASE_TAG = "//*[@id='mapSearch']/div[2]/"

    # 전체 건물리스트로 재접근을 위해 주소탭 클릭
    click_void(BASE_TAG + "div[3]/div/div[2]/div[2]/a", driver)
    # 주소탭 초기화
    click_void(
        BASE_TAG + "div[1]/section/div[1]/div[3]/div[1]/div/a[1]",
        driver,
    )
    # 시군구 주소 입력
    driver = select_sigungu(driver)
    # 지도에서 보기 클릭
    click_void(BASE_TAG + "div[1]/section/div[2]/a", driver)
    return driver


if __name__ == "__main__":
    move_to_page()
