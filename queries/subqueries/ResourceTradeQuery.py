class ResourceTradeQuery:
    __rss_check = ["coal", "iron", "lead", "bauxite", "oil", "uranium", "food", "steel", "aluminum", "gasoline", "munitions"]
    def __init__(self, rss: str):
        if not rss in self__rss_check:
            return None
            
        result = kit.legacyKit().query("trades", {"offer_resource": rss},
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