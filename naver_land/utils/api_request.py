import requests
import utils

# API request
# TODO : BaseCrawler 클래스 형성해 다른 크롤러들이 해당 클래스 상속받도록 수정
def get_request(self, url: str) -> requests.Response:
    header = utils.setup_header()
    response = requests.get(url, headers=header, allow_redirects=False)
    return response
