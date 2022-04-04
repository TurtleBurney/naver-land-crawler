"""
naver crawler

"""
from crawl_building import BuildingCrawler
from crawl_household import HouseholdCrawler


class NaverLandCrawler:
    """
    Naver Land Cralwer

    """

    def __init__(self) -> None:
        pass

    def run(self):
        # TODO : DB에서 region_code 읽어오기
        sample_region_code = "1141011000"

        # TODO : 반복문으로 building_id마다 크롤링
        building = BuildingCrawler(sample_region_code).run()
        household = HouseholdCrawler(building).run()
        # TODO : Building 정보 DB에 넣기


if __name__ == "__main__":
    # naver 부동산 정보 크롤링
    crawler = NaverLandCrawler()
    crawler.run()
