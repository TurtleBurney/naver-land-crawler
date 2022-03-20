import json
from region import Region
from region_extractor import RegionExtractor

SIDO = 0
SIGUGUN = 1
DONGEUP = 2


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
            region_names = address.split(" ")

            # 시/도 단위
            if len(region_names) == 1:
                self.get_level1_data(code, region_names)

            # 시도 + 시구군
            elif len(region_names) == 2:
                self.get_level2_data(code, region_names)

            # 시도 + 시구군 + 동읍면
            elif len(region_names) == 3:
                self.get_level3_data(code, region_names)

    def get_level1_data(self, code, region_names: list):
        region = Region(code, city=region_names[SIDO])
        self.regions.append(region.get())

    def get_level2_data(self, code, region_names: list):
        region = Region(
            code,
            city=region_names[SIDO],
            gu=region_names[SIGUGUN],
            parent_code=code[:2],
        )
        self.regions.append(region.get())

    def get_level3_data(self, code, region_names: list):
        region = Region(
            code,
            city=region_names[SIDO],
            gu=region_names[SIGUGUN],
            dong=region_names[DONGEUP],
            parent_code=code[:5],
        )
        self.regions.append(region.get())


if __name__ == "__main__":
    region_parser = RegionParser()
    region_parser.run()
