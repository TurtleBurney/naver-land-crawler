from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.main import create_app

# Deprecated
db = SQLAlchemy()
migrate = Migrate()

__all__ = [create_app]
