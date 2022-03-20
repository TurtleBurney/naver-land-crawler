from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def connect_database(app):
    # db객체가 declarative_base 대신 역할함(models에서 얘 상속받음)
    db.init_app(app)
    migrate.init_app(app, db)

    from database.models import household, issue, region, building, contract_price


def register_blueprints(app):
    # Blueprint
    from app.views import main, issue, updated_info, building

    app.register_blueprint(main.bp)

    app.register_blueprint(issue.bp_issue)
    app.register_blueprint(updated_info.bp_updated)
    app.register_blueprint(building.bp_building)
