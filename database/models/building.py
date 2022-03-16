from . import db


class Building(db.Model):
    building_id = db.Column(db.String(50), primary_key=True)

    building_name = db.Column(db.String(50), nullable=False)
    building_type = db.Column(
        db.Enum("APT", "OPT", name="building_type_enum"), nullable=False
    )

    dong_count = db.Column(db.Integer, nullable=False)
    household_count = db.Column(db.Integer, nullable=False)
    approval_date = db.Column(db.Date, nullable=False)

    lowest_floor = db.Column(db.Integer, nullable=False)
    highest_floor = db.Column(db.Integer, nullable=False)

    land_address = db.Column(db.String(100), nullable=False)
    road_address = db.Column(db.String(100), nullable=False)

    deal_count = db.Column(db.Integer, default=0)
    jeonse_count = db.Column(db.Integer, default=0)
    wolse_count = db.Column(db.Integer, default=0)

    # Foreign Key
    fk_region_code = db.Column(
        db.String(50), db.ForeignKey("region.region_code", ondelete="CASCADE")
    )

    # Back Reference
    households = db.relationship("Household", backref=db.backref("building"))
