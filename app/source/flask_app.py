from flask import Flask


# app/configs/config.py에서의 항목 불러옴
from app.configs import config
from app.source.db import connect_database, register_blueprints


def create_app(cfg=None):
    app = Flask(__name__)
    app.config.from_object(config)

    if cfg:
        app.config.update(cfg)

    connect_database(app)
    register_blueprints(app)

    return app


if __name__ == "__main__":
    create_app()