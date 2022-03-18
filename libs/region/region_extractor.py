import json


class RegionExtractor:
    def __init__(self, region_file_path) -> None:
        self.region_file_path = region_file_path
        self.dosigu = [
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

    def run(self) -> dict:
        region_data = self.load_region_data(self.region_file_path)

        region_data = self.refine_sejong_data(region_data)
        region_data = self.refine_dosigu_data(region_data)
        return region_data

    def load_region_data(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        region_data = json_data["존재"]
        return region_data

    def refine_sejong_data(self, region_data):
        for code, address in region_data.items():
            splitted_address = address.split(" ")

            # 세종시 문자열 처리
            if splitted_address[0] == "세종특별자치시":
                splitted_address.insert(1, "세종시")
                region_data[code] = " ".join(splitted_address)

        region_data["3600000000"] = "세종특별자치시"
        return region_data

    def refine_dosigu_data(self, region_data):
        for code, address in region_data.items():
            splitted_address = address.split(" ")

            # 도시구 문자열 처리
            # 경기도 고양시덕양구, 경기도 고양시덕양구 화정동
            if (len(splitted_address) >= 3) and (splitted_address[1] in self.dosigu):
                splitted_address[1] = splitted_address[1] + splitted_address[2]
                del splitted_address[2]
                region_data[code] = " ".join(splitted_address)
        return region_data
