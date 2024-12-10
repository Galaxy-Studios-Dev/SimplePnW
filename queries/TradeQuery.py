class TradeQuery:
    def __init__(self, page: int):
        if page == 0:
            return None
            
        if page > 0:
            result = kit.legacyKit().query("trades", {"page": page},
                         """
                         id
                         type
                         date
                         date_accepted
                         buy_or_sell
                         
                         offer_resource
                         offer_amount
                         price
                         
                         sender {
                            nation_name
                         }
                         
                         receiver {
                            nation_name
                         }
                         """).get()
            
            for data in result:
                print(f"{data}")
        