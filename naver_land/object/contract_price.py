class ContractPrice:
    def __init__(self, data: dict):
        self.contract_type = data["contract_type"]

        self.min_price = data["min_price"]
        self.max_price = data["max_price"]

        self.fk_household = data["fk_household"]

    def __str__(self) -> str:
        return f"<fk.household : {self.fk_household}, contract_type : {self.contract_type}, min_price : {self.min_price}, max_price : {self.max_price}>"

    def __repr__(self) -> str:
        return f"<fk.household : {self.fk_household}, contract_type : {self.contract_type}, min_price : {self.min_price}, max_price : {self.max_price}>"
