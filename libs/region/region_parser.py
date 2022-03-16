import json
from region import Region

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


class RegionParser:
    def __init__(self):
        self.regions = []

    def run(self):
        region_data = self.parse_region_json()
        self.get_region_code(region_data)
        with open("test.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(self.regions, ensure_ascii=False, indent="\t"))

    def parse_region_json(self) -> dict:
        PATH = "./data/region_code_name.json"
        with open(PATH, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        region_data = json_data["존재"]
        return region_data

    def get_region_code(self, region_data: dict):
        region_codes = list(region_data.keys())

        for code in region_codes:
            address = region_data[code]
            splitted_address = address.split(" ")

            # 시/도 단위
            if len(splitted_address) == 1:
                self.get_sido_data(code, splitted_address)

            # 세종시
            elif splitted_address[0] == SEJONG:
                if len(splitted_address) == 2:
                    self.get_sejong_data(code, splitted_address)

            # 도내 구를 가진 시
            elif splitted_address[1] in EXCEPTION:
                self.get_exception_region_data(code, splitted_address)

            # 일반적인 시(도)/구(군)/동읍면의 경우
            else:
                self.get_gudong_data(code, splitted_address)

    def get_sido_data(self, code, splitted_address: list):
        region = Region(code, city=splitted_address[0])
        self.regions.append(region.get())

    def get_sejong_data(self, code: list, splitted_address: list):
        # ex) 세종특별자치시 소정면, 세종특별자치시 반곡동
        parent_code = code[:5] + "00000"
        region = Region(
            code,
            city=splitted_address[0],
            dong=splitted_address[1],
            parent_code=parent_code,
        )
        self.regions.append(region.get())

    def get_exception_region_data(self, code: list, splitted_address: list):
        if len(splitted_address) == 2:
            pass

        elif len(splitted_address) == 3:
            parent_code = code[:2] + "00000000"
            gu = splitted_address[1] + " " + splitted_address[2]

            region = Region(
                code, city=splitted_address[0], gu=gu, parent_code=parent_code
            )
            self.regions.append(region.get())

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
            self.regions.append(region.get())

    def get_gudong_data(self, code, splitted_address):
        # 구/군 단위
        if len(splitted_address) == 2:
            parent_code = code[:2] + "00000000"

            region = Region(
                code,
                city=splitted_address[0],
                gu=splitted_address[1],
                parent_code=parent_code,
            )
            self.regions.append(region.get())

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
            self.regions.append(region.get())


if __name__ == "__main__":
    region_parser = RegionParser()
    region_parser.run()
