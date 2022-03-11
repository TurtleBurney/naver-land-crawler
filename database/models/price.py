from app import db

# from sqlalchemy.dialects.postgresql import ENUM


class Price(db.Model):
    price_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_type = db.Column(
        db.Enum("Deal", "Jeonse", "Wolse", name="sale_type_enum"), nullable=False
    )
    default_price = db.Column(db.Integer, nullable=False)
    highest_price = db.Column(db.Integer, nullable=True)
    wolse_price = db.Column(db.Integer, nullable=True)

    # Foreign Key
    fk_house_id = db.Column(
        db.Integer, db.ForeignKey("household.household_id", ondelete="CASCADE")
    )

