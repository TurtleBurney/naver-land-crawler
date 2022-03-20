class Region:
    def __init__(self, code, city, gu=None, dong=None):
        self.code = self.encode_region(code)
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

        # level 1(시, 도)의 경우
        if self.gu is None:
            return parent_code
        # level 2(시구군)의 경우
        elif self.dong is None:
            return self.encode_region(code[:2])
        else:
            return self.encode_region(code[:5])

    def encode_region(self, code):
        return code.ljust(10, "0")
