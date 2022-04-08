from object import ContractPrice


class ContractPriceCrawler:
    def __init__(self):
        pass

    def get_contract_price_list(self, response: "json"):
        contract_price_raw_list = response["result"]["list"]
        contract_price_info = []

        for i in range(len(contract_price_raw_list)):
            contract_price_raw = contract_price_raw_list[i]

            min_price = self.split_wolse(contract_price_raw["sameAddrMinPrc"])
            max_price = self.split_wolse(contract_price_raw["sameAddrMaxPrc"])

            contract_price_data = {
                "contract_type": contract_price_raw["tradTpNm"],
                "min_price": min_price["price"],
                "max_price": max_price["price"],
                "min_wolse_price": min_price["wolse"],
                "max_wolse_price": max_price["wolse"],
                "fk_household": contract_price_raw["atclNo"],
            }

            contract_price = ContractPrice(contract_price_data)
            contract_price_info.append(contract_price)
        return contract_price_info

    def split_wolse(self, price_raw: str) -> str:
        splitted_price = price_raw.split("/")

        price_dict = {"price": splitted_price[0], "wolse": 0}

        if len(splitted_price) == 2:
            price_dict["wolse"] = splitted_price[1]
        return price_dict
