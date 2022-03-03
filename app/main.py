from flask import Flask


# app/confconfig.py에서의 항목 불러옴
from app.configs import config
from app.source.db import connect_database, register_blueprints


def run():
    app = Flask(__name__)
    app.config.from_object(config)

    connect_database(app)
    register_blueprints(app)


if __name__ == "__main__":
    run()
