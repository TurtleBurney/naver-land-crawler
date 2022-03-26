import os
import json
from region import Region
from region_extractor import RegionExtractor

SIDO = 0
SIGUGUN = 1
DONGEUP = 2


class RegionParser:
    def __init__(self):
        self.input_file_path = (
            str(os.getcwd()) + "/libs/region" + "/data/region_code_name.json"
        )
        self.output_file_path = "test_2.json"
        self.regions = []

    def run(self):
        region_data = RegionExtractor(self.input_file_path).run()

        regions = self.parse_region(region_data)

        self.save_region_to_json(regions)
        self.regions = regions

    def parse_region(self, region_data: dict):
        regions = []
        for code, address in region_data.items():
            region_names = address.split(" ")

            region = Region(code, region_names).get()

            regions.append(region)
        return regions

    def save_region_to_json(self, regions):
        with open(self.output_file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(regions, ensure_ascii=False, indent="\t"))
