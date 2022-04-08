"""
naver crawler

"""
from crawler import BuildingCrawler, HouseholdCrawler, HouseholdPriceResponse
from pprint import pprint

sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class NaverLandCrawler:
    """
    Naver Land Cralwer

    """

    def __init__(self):
        pass

    def run(self) -> None:
        # TODO : DB에서 region_code 읽어오기
        sample_region_code = "1141011000"

        # TODO : 반복문으로 building_id마다 크롤링
        building = BuildingCrawler(sample_region_code).run()
        total_households = []
        total_contract_prices = []

        for sale_type in sale_type_enum:
            household_price_response = HouseholdPriceResponse(building, sale_type)

            sale_type_key = household_price_response.add_str_count(sale_type)
            page_count = household_price_response.calculate_total_page_num(
                sale_type_key
            )

            for page_num in range(1, page_count + 1):
                # get page response
                response = household_price_response.get_response_json(page_num)
                print(f"{sale_type} {page_num} 진행")

                household = HouseholdCrawler(building).get_household_list(
                    sale_type, page_num, response
                )
                # contract_price =
                total_households += household
        print(len(total_households))
        pprint(total_households)
        # total_contract_prices += contract_price
        # TODO : Building 정보 DB에 넣기


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
