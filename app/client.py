import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def click_javascript_void(xpath, driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "{0}".format(xpath)))
    ).click()

def select_sigungu(driver):
    # 주소 입력(시, 구, 동)
    BASE_TAG = "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/"

    click_javascript_void(BASE_TAG + "div[1]/div[2]/div/div/table/tbody/tr[1]/td[1]/a", driver)
    click_javascript_void(BASE_TAG + "div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/a", driver)
    click_javascript_void(BASE_TAG + "div[3]/div[2]/div/div/table/tbody/tr[3]/td[2]/a", driver)
    driver.implicitly_wait(20)
    return driver

def move_to_page(url):
    driver = webdriver.Chrome(os.path.join("libs", "chromedriver.exe"))
    driver.get(url)

    apt_btn = driver.find_element_by_class_name(
        "home_main_button.first_line._rletTypeBtn._innerLink"
    )
    apt_btn.click()
    BASE_TAG = "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/"
    # 주소 변경 탭 활성화
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[3]/div/div[2]/div[1]/a", driver)
    select_sigungu(driver)
    return driver

def move_to_each_page(driver, i):
    # 건물 선택하고 지도에서 보기로 이동
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[{0}]/a".format(i+1), driver)
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[1]/section/div[2]/a", driver)
    click_javascript_void("//*[@id='_listContainer']/div/div[3]/div/div/div[1]/a", driver)
    return driver

def move_back(driver):
    driver.back()
    driver.back()
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[3]/div/div[2]/div[2]/a", driver)
    # 주소탭 초기화
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/div[3]/div[1]/div/a[1]", driver)
    driver = select_sigungu(driver)
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[1]/section/div[2]/a", driver)
    return driver

if __name__ == "__main__":
    move_to_page()
