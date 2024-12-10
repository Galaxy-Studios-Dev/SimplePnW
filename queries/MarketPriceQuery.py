class MarketPriceQuery:
    __date_queried = ""
    __prices = {}

    def __init__(self, kit, first=0, page=0):
        if first == 0 and page == 0:
            return None
            
        if page > 0:
            result = kit.legacyKit().query("tradeprices", {"page": page},
                                                """
                                                date
    
                                                coal
                                                iron
                                                lead
                                                bauxite
                                                oil
                                                uranium
                                                food
                                                steel
                                                aluminum
                                                gasoline
                                                munitions
    
                                                """).get()
        elif first > 0 and first <= 1000:
            result = kit.legacyKit().query("tradeprices", {"first": first},
                                                """
                                                date
    
                                                coal
                                                iron
                                                lead
                                                bauxite
                                                oil
                                                uranium
                                                food
                                                steel
                                                aluminum
                                                gasoline
                                                munitions
    
                                                """).get()
    
            prices = result.tradeprices[0]
            self.__date_queried = prices.date
            self.__prices = {'coal': prices.coal, 'iron': prices.iron, 'lead': prices.lead, 'bauxite': prices.bauxite, 'oil': prices.oil, 'uranium': prices.uranium, 'food': prices.food, 'steel': prices.steel, 'aluminum': prices.aluminum, 'gasoline': prices.gasoline, 'munitions': prices.munitions}

    def dateRetreived(self):
        return self.__date_queried

    def prices(self):
        return self.__prices

    def price(self, key):
        return self.__prices[key]
