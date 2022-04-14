import requests
import time


class BaseCrawler:
    def __init__(self):
        self.naverURL = "https://m.land.naver.com"
        self.header = self.setup_header()

    def setup_header(self) -> dict:
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
        return header

    def send_request(self, url: str) -> requests.Response:
        response = requests.get(url, headers=self.header, allow_redirects=False)
        time.sleep(2)
        return response
