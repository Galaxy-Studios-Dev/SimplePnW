class WarQuery:
    def __init__(self, page: int):
        if page == 0:
            return None
        
        if page > 0:
            result = kit.legacyKit().query("wars", {"first": first},
                                     """
                                     date
                                     end_date
                                     reason
                                     turns_left
                                     
                                     ground_control
                                     air_superiority
                                     naval_blockade
                                     
                                     att_resistance
                                     att_points
                                     att_peace
                                     att_fortify
                                     
                                     att_soldiers_lost
                                     att_tanks_lost
                                     att_aircraft_lost
                                     att_ships_lost
                                     
                                     att_nukes_used
                                     
                                     att_steel_used
                                     att_alum_used
                                     att_gas_used
                                     att_munis_used
                                     
                                     att_infra_destroyed
                                     att_infra_destroyed_value
                                     
                                     attacker {
                                        id
                                        nation_name
                                     }
                                     
                                     def_resistance
                                     def_points
                                     def_peace
                                     def_fortify
                                     
                                     def_soldiers_lost
                                     def_tanks_lost
                                     def_aircraft_lost
                                     def_ships_lost
                                     
                                     def_nukes_used
                                     
                                     def_steel_used
                                     def_alum_used
                                     def_gas_used
                                     def_munis_used
                                     
                                     def_infra_destroyed
                                     def_infra_destroyed_value
                                     
                                     defender {
                                        id
                                        nation_name
                                     }
                                     
                                     attacks {
                                        date
                                        type
                                        
                                        resistance_lost
                                        infra_destroyed
                                        infra_destroyed_value
                                        improvements_destroyed
                                        
                                        loot_info
                                        money_looted
                                        coal_looted
                                        iron_looted
                                        lead_looted
                                        bauxite_looted
                                        oil_looted
                                        uranium_looted
                                        steel_looted
                                        aluminum_looted
                                        gasoline_looted
                                        munitions_looted
                                     
                                        attacker {
                                            nation_name
                                        }
                                        
                                        att_gas_used
                                        att_mun_used
                                        
                                        att_soldiers_used
                                        att_tanks_used
                                        att_aircraft_used
                                        att_ships_used
                                        
                                        att_soldiers_lost
                                        att_tanks_lost
                                        att_aircraft_lost
                                        att_ships_lost
                                        
                                        att_missiles_lost
                                        att_nukes_lost
                                        
                                        defender {
                                            nation_name
                                        }
                                        
                                        def_gas_used
                                        def_mun_used
                                        
                                        def_soldier_used
                                        def_tanks_used
                                        def_aircraft_used
                                        def_ships_used
                                        
                                        def_soldiers_lost
                                        def_tanks_lost
                                        def_aircraft_lost
                                        def_ships_lost
                                        
                                        def_missiles_lost
                                        def_nukes_lost
                                        
                                     }

                                     """).get()

            for data in result:
                print(f"{data}")