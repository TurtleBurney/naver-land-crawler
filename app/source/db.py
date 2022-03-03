from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def connect_database(app):
    # db객체가 declarative_base 대신 역할함(models에서 얘 상속받음)
    db = SQLAlchemy()
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    from database.models import (
        household,
        price,
        issue,
        region,
        building_basic,
        building_detail,
    )


def register_blueprints(app):
    # Blueprint
    from app.views import main_views, building_views, issue_views, updated_info_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(building_views.bp_building)
    app.register_blueprint(issue_views.bp_issue)
    app.register_blueprint(updated_info_views.bp_updated)
