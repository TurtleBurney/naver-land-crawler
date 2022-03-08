from bs4 import BeautifulSoup


class Refiner:
    def __init__(self, html: str):
        tags = self.parse_html(html)

        self.refine_title(tags["title"])
        self.refine_detail(tags["details"])
        self.refine_floor(tags["floors"][1].text)
        self.refine_address(
            tags["addresses"][2].text.split("addr")[1].split("realPriceInfoYn")[0]
        )
        self.refine_price(tags["prices"])

    def parse_html(self, html: str) -> dict:
        soup = BeautifulSoup(html, "html.parser")

        tags = {
            "title": soup.find("strong", "detail_complex_title"),
            "details": soup.find_all("span", "detail_data_item"),
            "floors": soup.find_all("span", "data"),
            "addresses": soup.find_all("script", type="text/javascript"),
            "prices": soup.find_all("em", "txt_price"),
        }
        return tags

    def refine_title(self, tags: dict):
        self.title = {"title": tags["title"].text}

    def refine_detail(self, tags: dict):
        self.detail = {
            "total_household": tags["details"][0].text[:-2],
            "total_dong": tags["details"][1].text,
            "approval_date": tags["details"][2].text,
        }

    def refine_floor(self, tags: dict):
        splitted_floor = tags.split("/")
        self.floor = {"low": splitted_floor[0], "high": splitted_floor[1][:-1]}

    def refine_address(self, tags: dict):
        splitted_address = tags.split(",")
        self.address = {
            "land": splitted_address[0][4:-2],
            "road": splitted_address[-2].split("'")[1],
        }

    def refine_price(self, tags: dict):
        self.price = {
            "deal": tags["prices"][0].text,
            "jeonse": tags["prices"][1].text,
            "wolse": tags["prices"][2].text,
        }

    def get_refined_data(self) -> dict:
        return {
            "title": self.title,
            "detail": self.detail,
            "floor": self.floor,
            "address": self.address,
            "price": self.price,
        }
