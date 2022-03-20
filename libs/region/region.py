class Region:
    def __init__(self, code, region_names):
        self.code = code

        city, gu, dong = self.process_region_names(region_names)
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

    def process_region_names(self, region_names):
        region_names += [None, None]

        city = region_names[0]
        gu = region_names[1]
        dong = region_names[2]

        return city, gu, dong

    def process_parent_code(self, code):
        parent_code = None

        # ~ dongeup
        if self.dong is not None:
            parent_code = self.encode_region(code[:5])

        # ~ sigugun
        elif self.gu is not None:
            parent_code = self.encode_region(code[:2])

        return parent_code

    def encode_region(self, code):
        return code.ljust(10, "0")
