import json
from region import Region
from region_extractor import RegionExtractor


class RegionParser:
    def __init__(self):
        self.regions = []

    def run(self):
        file_path = "./data/region_code_name.json"
        region_data = RegionExtractor(file_path).run()
        self.get_region_code(region_data)
        with open("test_1.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(self.regions, ensure_ascii=False, indent="\t"))

    def get_region_code(self, region_data: dict):
        for code, address in region_data.items():
            splitted_address = address.split(" ")

            # 시/도 단위
            if len(splitted_address) == 1:
                self.get_level1_data(code, splitted_address)

            # 세종시
            elif len(splitted_address) == 2:
                self.get_level2_data(code, splitted_address)

            # 도내 구를 가진 시
            elif len(splitted_address) == 3:
                self.get_level3_data(code, splitted_address)

    def get_level1_data(self, code, splitted_address: list):
        region = Region(code, city=splitted_address[0])
        self.regions.append(region.get())

    def get_level2_data(self, code, splitted_address: list):
        region = Region(
            code, city=splitted_address[0], gu=splitted_address[1], parent_code=code[:2]
        )
        self.regions.append(region.get())

    def get_level3_data(self, code, splitted_address: list):
        region = Region(
            code,
            city=splitted_address[0],
            gu=splitted_address[1],
            dong=splitted_address[2],
            parent_code=code[:5],
        )
        self.regions.append(region.get())


if __name__ == "__main__":
    region_parser = RegionParser()
    region_parser.run()
