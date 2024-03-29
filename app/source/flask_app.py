from flask import Flask

# app/configs/config.py에서의 항목 불러옴
from app.configs import config


def create_app(cfg=None):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config)

    if cfg:
        app.config.update(cfg)

    register_blueprints(app)

    return app


def register_blueprints(app):
    # Blueprint
    from app.views import building, issue, main, updated_info

    app.register_blueprint(main.bp)

    app.register_blueprint(issue.bp_issue)
    app.register_blueprint(updated_info.bp_updated)
    app.register_blueprint(building.bp_building)


if __name__ == "__main__":
    app = create_app()
