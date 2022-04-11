from object import Household


class HouseholdCrawler:
    def __init__(self):
        super().__init__()

    def refine(self, household_raw):
        household_data = {
            "household_code": household_raw["atclNo"],
            "building_dong": household_raw["bildNm"][:-1],
            "floor": household_raw["flrInfo"],
            "direction": household_raw["direction"],
            "supply_area": household_raw["spc1"],
            "private_area": household_raw["spc2"],
        }
        return household_data

    def get_household(self, data, building_code):
        return Household(data, building_code)
