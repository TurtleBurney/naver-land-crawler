from lib2to3.pytree import Base
from base_crawler import BaseCrawler


class HouseholdCrawler(BaseCrawler):
    def __init__(self, building_code: str):
        super.__init__(self)
