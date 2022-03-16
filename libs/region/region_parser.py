import json
from .region import Region

EXCEPTION = [
    "고양시",
    "성남시",
    "수원시",
    "안산시",
    "안양시",
    "용인시",
    "청주시",
    "천안시",
    "포항시",
    "창원시",
    "전주시",
]
SEJONG = "세종특별자치시"


def read_region_json(self) -> json:
    with open("./region_code_name.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


def get_region_code(json_data: json) -> list:
    region_data = json_data["존재"]
    region_codes = list(region_data.keys())
    regions = []
    for code in region_codes:
        address = region_data[code]
        splitted_address = address.split(" ")
        # 시/도 단위
        if len(splitted_address) == 1:
            region = Region(code, city=address)
            regions.append(region.get())

            continue
        if splitted_address[0] != SEJONG and splitted_address[1] not in EXCEPTION:
            # 구/군 단위
            if len(splitted_address) == 2:
                parent_code = code[:2] + "00000000"
                region = Region(
                    code,
                    city=splitted_address[0],
                    gu=splitted_address[1],
                    parent_code=parent_code,
                )
                regions.append(region.get())
            # 동/읍/면 단위
            elif len(splitted_address) == 3:
                parent_code = code[:5] + "00000"
                region = Region(
                    code,
                    city=splitted_address[0],
                    gu=splitted_address[1],
                    dong=splitted_address[2],
                    parent_code=parent_code,
                )
                regions.append(region.get())
        # 세종시 및 예외시들의 경우
        else:
            # 세종시
            if splitted_address[0] == SEJONG:
                if len(splitted_address) == 2:
                    sejong_region = get_sejong_data(code, splitted_address)
                    regions.append(sejong_region.get())
            else:
                # 도에 속한 구 있는 시들
                region = get_exception_region_data(code, splitted_address)
                regions.append(region.get())
    return regions


def get_sejong_data(code, splitted_address):
    # ex) 세종특별자치시 소정면, 세종특별자치시 반곡동
    parent_code = code[:5] + "00000"
    region = Region(
        code,
        city=splitted_address[0],
        dong=splitted_address[1],
        parent_code=parent_code,
    )
    return region


def get_exception_region_data(code, splitted_address):
    region = Region(code, city=None)
    if len(splitted_address) == 2:
        pass
    elif len(splitted_address) == 3:
        parent_code = code[:2] + "00000000"
        gu = splitted_address[1] + " " + splitted_address[2]
        region = Region(code, city=splitted_address[0], gu=gu, parent_code=parent_code)
    else:
        parent_code = code[:4] + "000000"
        gu = splitted_address[1] + " " + splitted_address[2]
        region = Region(
            code,
            city=splitted_address[0],
            gu=gu,
            dong=splitted_address[3],
            parent_code=parent_code,
        )
    return region


if __name__ == "__main__":
    pass
    # json_data = read_sigungu_json()
    # region_data = get_region_code(json_data)
