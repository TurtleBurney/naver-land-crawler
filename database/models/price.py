from app import db


class Price(db.Model):
    price_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_type = db.Column(
        db.Enum("Deal", "Jeonse", "Wolse", name="sale_type_enum"), nullable=False
    )
    
    # 단위 : 만 원
    min_price = db.Column(db.String(10), nullable=False)
    max_price = db.Column(db.String(10), nullable=False)
    wolse_price = db.Column(db.String(10), nullable=True)

    # Foreign Key
    fk_house_id = db.Column(
        db.Integer, db.ForeignKey("household.household_id", ondelete="CASCADE")
    )
