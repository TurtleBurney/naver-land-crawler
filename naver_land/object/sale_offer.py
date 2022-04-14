class SaleOffer:
    def __init__(self, data: dict):
        self.fk_household = data["fk_household"]

        self.sale_type = data["sale_type"]

        self.price = data["price"]
        self.wolse = data["wolse"]

    def __str__(self) -> str:
        return f"<fk.household : {self.fk_household}, sale_type : {self.sale_type}, price/deposit : {self.price} / {self.wolse}>"

    def __repr__(self) -> str:
        return f"<fk.household : {self.fk_household}, sale_type : {self.sale_type}, price/deposit : {self.price} / {self.wolse}>"
