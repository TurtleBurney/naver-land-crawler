from app import db

class BuildingDetail(db.Model):
    building_id = db.Column(db.Integer, primary_key=True)
    total_household = db.Column(db.Integer, nullable=False)
    lowest_floor = db.Column(db.Integer, nullable=False)
    highest_floor = db.Column(db.Integer, nullable=False)
    approval_date = db.Column(db.Date, nullable=False)
    total_dong = db.Column(db.Integer, nullable=False)
    number_address = db.Column(db.String(100), nullable=False) # 지번주소
    road_address = db.Column(db.String(100), nullable=False)
    total_deal = db.Column(db.Integer, nullable=False)
    total_jeonse = db.Column(db.Integer, nullable=False)
    total_wolse = db.Column(db.Integer, nullable=False)
