class Region:
    def __init__(self, code, city, gu=None, dong=None, parent_code=None):
        self.code = code
        self.city = city
        self.gu = gu
        self.dong = dong
        self.parent_code = parent_code

    def get(self):
        return {
            "region_code": self.code,
            "city": self.city,
            "gu": self.gu,
            "dong": self.dong,
            "parent_code": self.parent_code,
        }
