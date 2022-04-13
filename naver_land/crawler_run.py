"""
naver crawler

"""
import time
from pprint import pprint

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
        pass

    def run(self) -> None:
        # TODO : DB에서 region_code 읽어오기
        sample_region_code = "1141011000"

        households = []
        sale_offers = []

        household_crawler = HouseholdCrawler()
        sale_offer_crawler = SaleOfferCrawler()

        building_crawler = BuildingCrawler()
        buildings = self.crawl_building(building_crawler, sample_region_code)
        time.sleep(1)

        for building in buildings:
            household_count = 0

            household_list = self.crawl_household(
                household_crawler, building, sample_region_code
            )

            households += household_list
            household_count += len(household_list)
            time.sleep(1)

            for household in household_list:
                household_code = household.household_code
                # TODO : Cralwer도 param으로 넘기는게 맞는가 확인
                sale_offer_list = self.crawl_sale_offer(
                    sale_offer_crawler, household_code
                )

                sale_offers += sale_offer_list
                pprint(sale_offer_list)

            logger.info(
                f"building {building.building_code} Crawled >> household_count : {household_count}"
            )
            time.sleep(3)
        # TODO : Building 정보 DB에 넣기

    def crawl_building(
        self, building_crawler: BuildingCrawler, region_code: str
    ) -> list:
        building_crawler.set_region(region_code)
        buildings = building_crawler.crawl()

        return buildings

    def crawl_household(
        self,
        household_crawler: HouseholdCrawler,
        building: Building,
        region_code: str,
    ):
        building_code = building.building_code

        household_crawler.set_building_info(region_code, building_code)
        households_in_building = []

        for sale_type in sale_type_enum:
            household_crawler.set_sale_type(sale_type)
            household_page_num = building.get_household_page_num(sale_type)

            for page_idx in range(household_page_num):
                page_index = page_idx + 1

                household_list = household_crawler.crawl(page_index)
                households_in_building += household_list

        return households_in_building

    def crawl_sale_offer(
        self, sale_offer_crawler: SaleOfferCrawler, household_code: str
    ) -> list:
        sale_offer_crawler.set_household(household_code)

        sale_offer_list = sale_offer_crawler.crawl()
        return sale_offer_list


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
