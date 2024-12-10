class EmbargoesQuery:
    def __init__(self, kit, page: int):
        if page == 0:
            return None
        
        if page > 0:
            result = kit.legacyKit().query("embargoes", {"page": page},
                                     """
                                     date
                                     reason
                                     
                                     sender {
                                        id
                                        nation_name
                                     }
                                     
                                     receiver {
                                        id
                                        nation_name
                                     }

                                     """).get()
            
            for data in result:
                print(f"{data}")