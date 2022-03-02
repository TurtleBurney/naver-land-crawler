from app import db


class BuildingBasic(db.Model):
    building_id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(50), nullable=False)
    building_type = db.Column(
        db.Enum("A1", "B1", "B2", name="building_code_enum"), nullable=False
    )

    # Foreign Key
    region_code = db.Column(
        db.String(50), db.ForeignKey("region.region_code", ondelete="CASCADE")
    )

    # Back Reference
    # household 추가
