from config import CHROME_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def move_to_page(url):
    def click_javascript_void(xpath):
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "{0}".format(xpath)))
        ).click()

    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get(url)

    apt_btn = driver.find_element_by_class_name(
        "home_main_button.first_line._rletTypeBtn._innerLink"
    )
    apt_btn.click()
    base_tag = "//*[@id='mapSearch']/div[2]/div[1]/section/div[1]/"
    # 주소 변경 탭 활성화
    click_javascript_void("//*[@id='mapSearch']/div[2]/div[3]/div/div[2]/div[1]/a")
    # 주소 입력(시, 구, 동)
    click_javascript_void(base_tag + "div[1]/div[2]/div/div/table/tbody/tr[1]/td[1]/a")
    click_javascript_void(base_tag + "div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]/a")
    click_javascript_void(base_tag + "div[3]/div[2]/div/div/table/tbody/tr[3]/td[2]/a")
    driver.implicitly_wait(20)
    return driver


if __name__ == "__main__":
    move_to_page()
