from app import db


class Building(db.Model):
    building_id = db.Column(db.String(50), primary_key=True)

    building_name = db.Column(db.String(50), nullable=False)
    building_type = db.Column(
        db.Enum("A1", "B1", "B2", name="building_code_enum"), nullable=False
    )
    total_household = db.Column(db.Integer, nullable=False)
    approval_date = db.Column(db.Date, nullable=False)
    total_dong = db.Column(db.Integer, nullable=False)

    lowest_floor = db.Column(db.Integer, nullable=False)
    highest_floor = db.Column(db.Integer, nullable=False)

    land_address = db.Column(db.String(100), nullable=False)  
    road_address = db.Column(db.String(100), nullable=False)

    total_deal = db.Column(db.Integer, nullable=False)
    total_jeonse = db.Column(db.Integer, nullable=False)
    total_wolse = db.Column(db.Integer, nullable=False)

    # Foreign Key
    fk_region_code = db.Column(
        db.String(50), db.ForeignKey("region.region_code", ondelete="CASCADE")
    )

    # Back Reference
    households = db.relationship(
        "Household", backref=db.backref("building", cascade="all, delete-orphan")
    )
