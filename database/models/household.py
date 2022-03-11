from app import db
from sqlalchemy.sql import func


class Household(db.Model):
    household_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dong = db.Column(db.Integer, nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.String(10), nullable=False)
    area = db.Column(db.Float, nullable=False)
    link = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # Foreign key
    fk_building_id = db.Column(
        db.String(50), db.ForeignKey("building.building_id", ondelete="CASCADE")
    )

    # Back Reference
    prices = db.relationship(
        "Price", backref=db.backref("household", cascade="all, delete-orphan")
    )
