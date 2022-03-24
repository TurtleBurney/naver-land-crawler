from app.source.db import db
from app.source.flask_app import create_app


class DBStorer:
    def __init__(self, model):
        self.model = model

    def add_data(self, data):
        self.data = data
        app = create_app()
        app.app_context().push()
        db.session.bulk_insert_mappings(self.model, data)
        db.session.commit()
