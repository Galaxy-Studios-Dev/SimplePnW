class MarketPrices:
    __kit = {}
    __index = 0

    __query = {}

    def __init__(self, kit, page_index):
        self.__kit = kit
        self.__index = page_index

        self.__query = self.__kit.query("prices", self.__index)

    def requery(self):
        self.__query = self.__kit.query("prices", self.__index)