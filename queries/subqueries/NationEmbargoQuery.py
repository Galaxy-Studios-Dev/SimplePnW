class NationEmbargoQuery:
    def __init__(self, kit, nation_id: int):
        result = kit.legacyKit().query("embargoes", {"id": nation_id},
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