class NationTradeQuery:
    def __init__(self, nation_id: int):
        result = kit.legacyKit().query("trades", {"nation_id": nation_id},
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