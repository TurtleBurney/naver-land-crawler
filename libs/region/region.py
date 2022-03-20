class Region:
    def __init__(self, code, city, gu=None, dong=None):
        self.code = code

        self.city = city
        self.gu = gu
        self.dong = dong

        self.parent_code = self.process_parent_code(code)

    def get(self):
        return {
            "region_code": self.code,
            "city": self.city,
            "gu": self.gu,
            "dong": self.dong,
            "parent_code": self.parent_code,
        }

    def process_parent_code(self, code):
        parent_code = None

        # level 3
        if self.dong is not None:
            parent_code = self.encode_region(code[:5])
        # level 2
        elif self.gu is not None:
            parent_code = self.encode_region(code[:2])

        return parent_code

    def encode_region(self, code):
        return code.ljust(10, "0")
