class Household:
    def __init__(self, data: dict, building_code: str):
        self.household_code = data["household_code"]

        self.building_dong = data["building_dong"]
        self.floor = data["floor"]
        self.direction = data["direction"]

        self.supply_area = data["supply_area"]
        self.private_area = data["private_area"]

        self.fk_building_id = building_code

    def __str__(self) -> str:
        return f"<code : {self.household_code}, building_dong : {self.building_dong}, floor : {self.floor}, direction : {self.direction}, supply_area : {self.supply_area}, private_area : {self.private_area}>"

    def __repr__(self) -> str:
        return f"<code : {self.household_code}, building_dong : {self.building_dong}, floor : {self.floor}, direction : {self.direction}, supply_area : {self.supply_area}, private_area : {self.private_area}>"
