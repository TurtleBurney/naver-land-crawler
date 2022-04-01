import requests


class BaseCrawler:
    def __init__(self):
        self.baseURL = "https://m.land.naver.com/complex"

    def setup_header(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
        return header

    def get_request(self, url: str) -> requests.Response:
        header = self.setup_header()
        response = requests.get(url, headers=header, allow_redirects=False)
        return response
