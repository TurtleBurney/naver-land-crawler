import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def click_void(driver, tag):
    WebDriverWait(driver, 500).until(
        EC.element_to_be_clickable((By.XPATH, f"{tag}"))
    ).click()


def init_driver(url):
    driver = webdriver.Chrome(os.path.join("libs", "chromedriver.exe"))
    driver.get(url)
    return driver


if __name__ == "__main__":
    init_driver()
