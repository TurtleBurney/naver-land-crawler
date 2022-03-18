class Region:
    def __init__(self, code, city, gu=None, dong=None, parent_code=None):
        self.code = self.encode_region(code)
        self.city = city
        self.gu = gu
        self.dong = dong
        self.parent_code = self.process_parent_code(parent_code)

    def get(self):
        return {
            "region_code": self.code,
            "city": self.city,
            "gu": self.gu,
            "dong": self.dong,
            "parent_code": self.parent_code,
        }

    def process_parent_code(self, parent_code):
        if parent_code is None:
            return parent_code
        else:
            return self.encode_region(parent_code)

    def encode_region(self, code):
        return code.ljust(10, "0")
