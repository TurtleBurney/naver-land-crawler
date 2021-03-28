import os
import json
import requests


# @router.post("kakao/send")
def send_kakao():
    assert os.environ["KAKAO_TOKEN"] is not None
    token = os.environ["KAKAO_TOKEN"]

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": f"Bearer {token}"}
    body = json.dumps(
        {
            "object_type": "text",
            "text": "ARI UNDUNGE",
            "link": {"web_url": "www.naver.com"},
        }
    )

    data = {"template_object": body}

    try:
        response = requests.post(url, headers=headers, data=data)
        code = response.status_code
        if code != 200:
            raise
    except Exception:
        raise

    return response


if __name__ == "__main__":
    send_kakao()
