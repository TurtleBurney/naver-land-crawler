from database import session


class DBStorer:
    def __init__(self, model):
        self.model = model

    def add_data(self, data):
        self.data = data
        session.bulk_insert_mappings(self.model, data)
        session.commit()
