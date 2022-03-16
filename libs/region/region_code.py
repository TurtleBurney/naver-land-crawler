import json
# from database.models.region import Region
EXCEPTION = ['고양시', '성남시', '수원시', '안산시', '안양시', '용인시', '청주시', '천안시', '포항시', '창원시', '전주시']
SEJONG = '세종특별자치시'

def read_sigungu_json() -> json:
    with open('./region_code_name.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data

def get_region_code(json_data: json):
    region_data = json_data["존재"]
    region_codes = list(region_data.keys())
    regions = []
    for code in region_codes:
        address = region_data[code]
        splitted_address = address.split(" ")
        # 예외에 해당 안한는 일반 CASE
            # 시/도 단위
        if(len(splitted_address) == 1):
            regions.append({
                'region_code' : code,
                'city' : address,
            })
            continue
        if (splitted_address[0] != SEJONG and splitted_address[1] not in EXCEPTION):
            # 구/군 단위
            if (len(splitted_address) == 2):
                parent_code = code[:2] + '00000000'
                regions.append({
                    'region_code' : code,
                    'city' : splitted_address[0],
                    'gu' : splitted_address[1],
                    'parent_code' : parent_code
                })
            # 동/읍/면 단위
            elif (len(splitted_address) == 3):
                parent_code = code[:5] + '00000'
                regions.append({
                    'region_code' : code,
                    'city' : splitted_address[0],
                    'gu' : splitted_address[1],
                    'dong' : splitted_address[2],
                    'parent_code' : parent_code
                })
        # 세종시 및 예외시들의 경우
        else:
            # 세종시
            if (splitted_address[0] == SEJONG):
                if len(splitted_address) != 2:
                    continue
                # ex) 세종특별자치시 소정면, 세종특별자치시 반곡동
                parent_code = code[:5] + "00000"
                regions.append({
                    'region_code' : code,
                    'city' : splitted_address[0],
                    'dong' : splitted_address[1],
                    'parent_code' : parent_code
                })
            # 도에 속한 구 있는 시들
            else:
                if len(splitted_address) == 2:
                    continue
                elif len(splitted_address) == 3:
                    parent_code = code[:2] + '00000000'
                    gu = splitted_address[1] + ' ' + splitted_address[2]
                    regions.append({
                    'region_code' : code,
                    'city' : splitted_address[0],
                    'gu' : gu,
                    'parent_code' : parent_code
                })
                else:
                    parent_code = code[:4] + '000000'
                    gu = splitted_address[1] + ' ' + splitted_address[2]
                    regions.append({
                    'region_code' : code,
                    'city' : splitted_address[0],
                    'gu' : gu,
                    'dong' : splitted_address[3],
                    'parent_code' : parent_code
                })

if __name__ == "__main__":
    json_data = read_sigungu_json()
    get_region_code(json_data)


