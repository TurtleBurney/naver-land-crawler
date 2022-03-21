from app.source.db import db
from app.source.flask_app import create_app


class DbStorer:
    def __init__(self, model, data: dict):
        self.model = model
        self.data = data

    def run(self):
        # model에 맞게 포맷 변경(향후 다른 model data 삽입시 수정)
        # db 삽입
        self.store_data_at_db(self.model, self.data)

    def store_data_at_db(self, model, data):
        app = create_app()
        app.app_context().push()
        db.session.bulk_insert_mappings(model, data)
        db.session.commit()
