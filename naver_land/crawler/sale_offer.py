from crawler.base import BaseCrawler
from logger import init_logger
from object import SaleOffer

logger = init_logger()


class SaleOfferCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.household_code = None

    def set_household(self, household_code: str) -> None:
        self.household_code = household_code

    def crawl(self) -> list:
        # Step 1
        url = self.sale_offer_url(self.household_code)
        json_response = self.send_request(url).json()

        sale_offer_list = json_response
        sale_offers = []

        # Step 2
        for offer in sale_offer_list:
            sale_offer_data = {
                "fk_household": offer["atclNo"],
                "sale_type": offer["tradTpCd"],
                "price": offer["prc"],
                "wolse": offer["rentPrc"],
            }
            sale_offer = SaleOffer(sale_offer_data)
            sale_offers.append(sale_offer)

        return sale_offers

    def sale_offer_url(self, household_code: str) -> str:
        url = f"{self.naverURL}/article/getSameAddrArticle?articleNo={household_code}"
        return url
