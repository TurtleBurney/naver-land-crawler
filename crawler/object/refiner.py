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

    def refine_title(self, title_tag: dict):
        self.title = {"title": title_tag.text}

    def refine_detail(self, detail_tag: dict):
        self.detail = {
            "total_household": detail_tag[0].text[:-2],
            "total_dong": detail_tag[1].text[2:][:-1],
            "approval_date": detail_tag[2].text,
        }

    def refine_floor(self, floor_tag: dict):
        splitted_floor = floor_tag.split("/")
        self.floor = {"low": splitted_floor[0], "high": splitted_floor[1][:-1]}

    def refine_address(self, address_tag: dict):
        splitted_address = address_tag.split(",")
        self.address = {
            "land": splitted_address[0][4:-2],
            "road": splitted_address[-2].split("'")[1],
        }

    def refine_price(self, price_tag: dict):
        self.price = {
            "deal": price_tag[0].text,
            "jeonse": price_tag[1].text,
            "wolse": price_tag[2].text,
        }

    def get_refined_data(self) -> dict:
        return {
            "title": self.title,
            "detail": self.detail,
            "floor": self.floor,
            "address": self.address,
            "price": self.price,
        }
