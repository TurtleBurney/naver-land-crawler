# 아파트 정보 추출
# 매물 수가 0보다 크면 서치해라

specific_data = []

"""
e편한 오피스텔 : //*[@id="mapSearch"]/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[1]/a
e편한 아파트   : //*[@id="mapSearch"]/div[2]/div[1]/section/div[1]/div[4]/div/div[2]/div/ul/li[2]/a
li[x] (x = 1, 2, ..., len(ahyun))
"""
for x in range(len(ahyun)):
    if int(ahyun[x][1]) > 0:  # 매매 매물이 있을 때
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
        # 매매로 이동
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='_basic_content_cd']/div[1]/div[4]/ul/li[1]/a")
            )
        ).click()
        driver.implicitly_wait(50)

        # 각 매물에 접근
        # for i in range(int(ahyun[x][1])):
        building_name = driver.find_elements(By.CLASS_NAME, "title_place")
        building_dong = driver.find_elements(By.CLASS_NAME, "title_building")
        # 새로운 데이터타입 만드는게 우선(그 다음 각 아파트에 대한 매물 정보 저장)
        print(building_dong[0].text)
        # driver.quit()