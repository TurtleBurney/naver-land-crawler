"""
naver crawler

"""
import time
from pprint import pprint

from crawler import BuildingCrawler, HouseholdCrawler, SaleOfferCrawler
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
        sale_offers = []

        household_cralwer = HouseholdCrawler()
        sale_offer_crawler = SaleOfferCrawler()

        building_crawler = BuildingCrawler()
        building_crawler.set_region(sample_region_code)
        buildings = building_crawler.crawl()

        for building in buildings:
            building_code = building.building_code

            household_cralwer.set_building_info(sample_region_code, building_code)
            household_count = 0
            for sale_type in sale_type_enum:
                household_cralwer.set_sale_type(sale_type)
                household_page_num = building.get_household_page_num(sale_type)

                for page_idx in range(household_page_num):
                    page_index = page_idx + 1

                    household_list = household_cralwer.crawl(page_index)
                    households += household_list

                    for household in household_list:
                        sale_offer_crawler.set_household(household.household_code)

                        sale_offer_list = sale_offer_crawler.crawl()
                        sale_offers += sale_offer_list
                        pprint(sale_offer_list)

            logger.info(
                f"building {building_code} Crawled >> household_count : {household_count}"
            )
            time.sleep(3)
        # TODO : Building 정보 DB에 넣기


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
