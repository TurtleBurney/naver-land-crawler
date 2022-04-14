"""
naver crawler

"""
import time

from crawler import BuildingCrawler, HouseholdCrawler, SaleOfferCrawler
from object import Building
from logger import init_logger

logger = init_logger()

sale_type_enum = {"deal": "A1", "jeonse": "B1", "wolse": "B2"}


class NaverLandCrawler:
    """
    Naver Land Cralwer

    """

    def __init__(self):
        self.building_crawler = BuildingCrawler()
        self.household_crawler = HouseholdCrawler()
        self.sale_offer_crawler = SaleOfferCrawler()

    def run(self) -> None:
        # TODO : DB에서 region_code 읽어오기
        SAMPLE_REGION_CODE = "1141011000"

        households = []
        sale_offers = []

        buildings = self.crawl_building(SAMPLE_REGION_CODE)

        for building in buildings:
            households += self.crawl_household(building, SAMPLE_REGION_CODE)
            logger.info(
                f"household of building {building.building_code} Crawled >> household_count : {len(households)}"
            )
            time.sleep(3)

        for household in households:
            household_code = household.household_code

            sale_offers += self.crawl_sale_offer(household_code)
            logger.info(
                f"Sale Offer of household {household.household_code} Crawled >> sale_offer_count : {len(sale_offers)}"
            )
            time.sleep(3)

        # TODO : Building 정보 DB에 넣기

    def crawl_building(self, region_code: str) -> list:
        crawler = self.building_crawler

        crawler.set_region(region_code)
        buildings = crawler.crawl()

        return buildings

    def crawl_household(
        self,
        building: Building,
        region_code: str,
    ):
        crawler = self.household_crawler

        building_code = building.building_code

        crawler.set_building_info(region_code, building_code)
        households_in_building = []

        for sale_type in sale_type_enum:
            crawler.set_sale_type(sale_type)
            household_page_num = building.get_household_page_num(sale_type)

            for page_idx in range(household_page_num):
                page_index = page_idx + 1

                household_list = crawler.crawl(page_index)
                households_in_building += household_list

        return households_in_building

    def crawl_sale_offer(self, household_code: str) -> list:
        crawler = self.sale_offer_crawler

        crawler.set_household(household_code)
        sale_offer_list = crawler.crawl()
        return sale_offer_list


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
