from object import ContractPrice


class ContractPriceCrawler:
    def __init__(self):
        super().__init__()

    def refine(self, data):
        contract_price_data = {
            "contract_type": data["tradTpNm"],
            "min_price": data["sameAddrMinPrc"],
            "max_price": data["sameAddrMaxPrc"],
            "fk_household": data["atclNo"],
        }
        return contract_price_data

    def get_contract_price(self, data):
        return ContractPrice(data)
