from flask import Flask
from server.main.index import main as main
# app = Flask(__name__)

"""
어플리케이션 팩토리
app 객체를 전역으로 사용할 때 발생하는 순환 참조 문제를 예방
https://wikidocs.net/81504
"""
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'hello world!'
    return app


if __name__ == "__main__":
    app = create_app()
    app.register_blueprint(main) # 이건 왜 안 돼..?