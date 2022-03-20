import json


class RegionExtractor:
    def __init__(self, region_file_path="./data/region_code_name.json") -> None:
        self.region_file_path = region_file_path

    def run(self) -> dict:
        region_json = self.load_region_json(self.region_file_path)

        existing_region = self.filter_existing_data(region_json)
        valid_region = self.filter_valid_data(existing_region)

        region_data = self.refine_sejong_data(valid_region)
        region_data = self.refine_dosigu_data(region_data)

        return region_data

    def load_region_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
        return json_data

    def filter_existing_data(self, json_data):
        region_data = json_data["존재"]
        return region_data

    def filter_valid_data(self, region_data):
        valid_data = dict()
        for key, value in region_data.items():
            if key[-2:] == "00":
                valid_data[key] = value

        return valid_data

    def refine_sejong_data(self, region_data):
        for code, region in region_data.items():
            region_names = region.split(" ")

            # 세종시 문자열 처리
            if region_names[0] == "세종특별자치시":
                region_names.insert(1, "세종시")
                region_data[code] = " ".join(region_names)

        region_data["3600000000"] = "세종특별자치시"
        return region_data

    def refine_dosigu_data(self, region_data):
        dosigu = [
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

        for code, region in region_data.items():
            region_names = region.split(" ")

            # 도시구 문자열 처리
            # 경기도 고양시덕양구, 경기도 고양시덕양구 화정동
            if (len(region_names) >= 3) and (region_names[1] in dosigu):
                region_names[1] = region_names[1] + region_names[2]
                del region_names[2]
                region_data[code] = " ".join(region_names)
        return region_data
