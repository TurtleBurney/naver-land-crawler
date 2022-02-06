from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# config.py에서의 항목 불러옴
import config

db = SQLAlchemy()
migrate = Migrate()

"""
어플리케이션 팩토리
app 객체를 전역으로 사용할 때 발생하는 순환 참조 문제를 예방
https://wikidocs.net/81504
"""
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app


if __name__ == "__main__":
    app = create_app()