class Building():
    def __init__(self, data: dict):
        self.building_name = data["title"]["title"]

        self.total_household = data["details"]["total_household"]
        self.total_dong = data["details"]["total_dong"]
        self.approval_date = data["details"]["approval_date"]

        self.lowest_floor = data["floors"]["low"]
        self.highest_floor = data["floors"]["high"]

        self.land_address = data["addresses"]["land"]
        self.road_address = data["addresses"]["road"]

        self.total_deal = data["prices"]["deal"]
        self.total_jeonse = data["prices"]["jeonse"]
        self.total_wolse = data["prices"]["wolse"]
   

    def get_info(self) -> dict:
        return {
            "building_name" : self.building_name,

            "total_household" : self.total_household,
            "total_dong" : self.total_dong,
            "approval_date" : self.approval_date,

            "lowest_floor" : self.lowest_floor,
            "highest_floor" : self.highest_floor,

            "land_address" : self.land_address,
            "road_address" : self.road_address,

            "total_deal" : self.total_deal,
            "total_jeonse" : self.total_jeonse,
            "total_wolse" : self.total_wolse
        }

    def get_price_info(self) -> dict:
        return {
            "total_deal" : self.total_deal,
            "total_jeonse" : self.total_jeonse,
            "total_wolse" : self.total_wolse
        }
    

