import json
from bs4 import BeautifulSoup
import requests
# from app.models.building import Building

USER_AGENT_HEADER = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
BUILDING_LIST_URL = "https://m.land.naver.com/complex/ajax/complexListByCortarNo?cortarNo="
BUILDING_DETAIL_URL_HEAD = "https://m.land.naver.com/complex/info/"
BUILDING_DETAIL_URL_TAIL = "?tradTpCd=A1:B1:B2&ajax=y"

def make_request(url):
    header = {'user-agent' : USER_AGENT_HEADER}
    response = requests.get(url, headers=header, allow_redirects=False)
    return response

def get_building_json(code):
    url = BUILDING_LIST_URL + str(code)
    response = make_request(url)
    return response.json()

def get_detail_building_text(hscpNo):
    url = BUILDING_DETAIL_URL_HEAD + str(hscpNo) + BUILDING_DETAIL_URL_TAIL
    response = make_request(url)
    return response.text

# 건물 목록 + 건물 detail 정보 필요
def filter_building_info(basic_info):
    building_info = basic_info["result"][0]
    building_name = building_info["hscpNm"]
    building_type = building_info["hscpTypeNm"]
    total_deal = building_info["dealCnt"]
    total_jeonse = building_info["leaseCnt"]
    total_wolse = building_info["rentCnt"]
    return 

if __name__ == "__main__":
    target_html = get_detail_building_text(110209) 
    # soup = BeautifulSoup(target_html, "html.parser")
    # # print(soup.prettify())
    # file = open('sample.html', 'w', encoding="UTF-8")
    # file.write(target_html)
    # file.close()

    # 선택의 시간 두둥
    # 파라미터가 많은 복잡한 url VS html에서 태그찾기
    # https://m.land.naver.com/cluster/ajax/complexList?itemId=110209&mapKey=&lgeo=21221003332101&rletTpCd=OBYG:ABYG:OPST:APT:JGC&tradTpCd=A1:B1:B2&z=18&lat=37.558609&lon=126.951802&btm=37.5566167&lft=126.9496884&top=37.5606013&rgt=126.9539156&isOnlyIsale=false