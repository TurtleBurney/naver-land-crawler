"""
naver crawler

"""
from crawler import (
    BuildingCrawler,
    ContractPriceCrawler,
    HouseholdCrawler,
    HouseholdPriceCrawler,
)
import time
from logger import init_logger

logger = init_logger()
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

        households = []
        contract_prices = []

        household_cralwer = HouseholdCrawler()
        contract_price_crawler = ContractPriceCrawler()
        householdPriceResponse = HouseholdPriceCrawler()

        # TODO : 반복문으로 building_id마다 크롤링
        building_crawler = BuildingCrawler()
        building_crawler.set_region(sample_region_code)
        buildings = building_crawler.crawl()

        for building in buildings:
            building_code = building.building_code

            householdPriceResponse.set_building_info(building)
            household_count = 0
            for sale_type in sale_type_enum:
                householdPriceResponse.set_sale_type(sale_type)
                household_page_num = building.get_household_page_num(sale_type)

                for page_idx in range(household_page_num):
                    page_index = page_idx + 1

                    response = householdPriceResponse.crawl(page_index)

                    # Household From response
                    raw_response_list = response["result"]["list"]

                    for raw_response in raw_response_list:
                        household_data = household_cralwer.refine(raw_response)
                        household = household_cralwer.get_household(
                            household_data, building_code
                        )
                        households.append(household)
                        household_count += 1

                        contract_price_data = contract_price_crawler.refine(
                            raw_response
                        )
                        contract_price = contract_price_crawler.get_contract_price(
                            contract_price_data
                        )
                        contract_prices.append(contract_price)
            logger.info(
                f"building {building_code} Crawled >> household_count : {household_count}"
            )
            time.sleep(3)
        # TODO : Building 정보 DB에 넣기


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
