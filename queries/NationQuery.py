class NationQuery:
    __name = ""
    __leader_name = ""
    __founded = ""
    __last_active = ""
    __discord = ""
    __vmode = False

    __flag = ""
    __population = 0
    __color_block = ""
    __score = 0
    __continent = ""

    __resources = {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0, 'food': 0, 'gasoline': 0, 'munitions': 0, 'steel': 0, 'aluminum': 0, 'money': 0}

    __projects = {}

    __cities = {}

    __baseball_team = {}

    __troops = {'soldiers': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0},
                'tanks': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0},
                'aircraft': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0},
                'ships': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0},
                'spies': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0},
                'missiles': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0},
                'nukes': {'total': 0, 'casualties': 0, 'kills': 0, 'max-recruit': 0}
                }

    __war_policy = ""

    __war_policy_turns = 0
    __wars_won = 0
    __wars_lost = 0

    __offensive_wars_count = 0
    __defensive_wars_count = 0

    __wars = {}

    __alliance = {}
    __aa_join_date = ""
    __aa_position = ""
    __aa_seniority = ""


    def __init__(self, simple_pw, nation_id):
        result = simple_pw.legacyKit().query("nations", {"id": nation_id, "first": 1},
                                                """
                                                id
                                                nation_name
                                                leader_name
                                                date
                                                last_active
                                                discord
                                                vmode
                                                
                                                flag
                                                score
                                                population
                                                color
                                                continent
                                                
                                                coal
                                                iron
                                                lead
                                                bauxite
                                                oil
                                                uranium
                                                food
                                                gasoline
                                                munitions
                                                steel
                                                aluminum
                                                money
                                                
                                                activity_center
                                                advanced_engineering_corps
                                                advanced_pirate_economy
                                                advanced_urban_planning
                                                arable_land_agency
                                                arms_stockpile
                                                bauxite_works
                                                bureau_of_domestic_affairs
                                                center_for_civil_engineering
                                                central_intelligence_agency
                                                clinical_research_center
                                                emergency_gasoline_reserve
                                                fallout_shelter
                                                green_technologies
                                                government_support_agency
                                                guiding_satellite
                                                international_trade_center
                                                iron_dome
                                                iron_works
                                                mars_landing
                                                mass_irrigation
                                                metropolitan_planning
                                                military_salvage
                                                missile_launch_pad
                                                moon_landing
                                                nuclear_launch_facility
                                                nuclear_research_facility
                                                pirate_economy
                                                propaganda_bureau
                                                recycling_initiative
                                                research_and_development_center
                                                space_program
                                                specialized_police_training_program
                                                spy_satellite
                                                surveillance_network
                                                telecommunications_satellite
                                                uranium_enrichment_program
                                                urban_planning
                                                vital_defense_system
                                                
                                                cities {
                                                    id
                                                    name
                                                    date
                                                    nuke_date
                                                    infrastructure
                                                    land
                                                    
                                                    powered
                                                    coal_power
                                                    oil_power
                                                    nuclear_power
                                                    wind_power
                                                    
                                                    barracks
                                                    factory
                                                    hangar
                                                    drydock
                                                    
                                                    farm
                                                    coal_mine
                                                    iron_mine
                                                    lead_mine
                                                    bauxite_mine
                                                    oil_well
                                                    uranium_mine
                                                    
                                                    steel_mill
                                                    aluminum_refinery
                                                    oil_refinery
                                                    munitions_factory
                                                    
                                                    police_station
                                                    hospital
                                                    recycling_center
                                                    subway
                                                    
                                                    supermarket
                                                    bank
                                                    shopping_mall
                                                    stadium
                                                }
                                                
                                                baseball_team {
                                                    name
                                                    
                                                    logo
                                                    stadium
                                                    
                                                    home_jersey
                                                    away_jersey
                                                    
                                                    wins
                                                    glosses
                                                    games_played
                                                    
                                                    strikeouts
                                                    homers
                                                    
                                                    players {
                                                        name
                                                        position
                                                        age
                                                        birthday
                                                        overall
                                                    }
                                                }
                                                
                                                soldiers
                                                soldier_casualties
                                                soldier_kills
                                                soldiers_today
                                                
                                                tanks
                                                tank_casualties
                                                tank_kills
                                                tanks_today
                                                
                                                aircraft
                                                aircraft_casualties
                                                aircraft_kills
                                                aircraft_today
                                                
                                                ships
                                                ship_casualties
                                                ship_kills
                                                ships_today
                                                
                                                spies
                                                spy_casualties
                                                spy_kills
                                                spies_today
                                                
                                                missiles
                                                missile_casualties
                                                missile_kills
                                                missiles_today
                                                
                                                nukes
                                                nuke_casualties
                                                nuke_kills
                                                nukes_today
                                                
                                                war_policy
                                                war_policy_turns
                                                wars_won
                                                wars_lost
                                                
                                                offensive_wars_count
                                                defensive_wars_count
                                                
                                                wars {
                                                  date
                                                }
                                                
                                                alliance {
                                                    name
                                                    id
                                                    flag
                                                    
                                                    nations {
                                                        nation_name
                                                        leader_name
                                                        alliance_join_date
                                                        alliance_position
                                                        alliance_seniority
                                                    }
                                                }
                                                
                                                alliance_join_date
                                                alliance_position
                                                alliance_seniority
                                                """).get()

        nation = result.nations[0]
        self.__id = nation.id
        self.__name = nation.nation_name
        self.__founded = nation.date
        self.__last_active = nation.last_active
        self.__discord = nation.discord

        self.__flag = nation.flag
        self.__population = nation.population
        self.__score = nation.score
        self.__continent = nation.continent
        self.__color_block = nation.color
        
        self.__resources = {'coal': nation.coal, 'iron': nation.iron, 'lead': nation.lead, 'bauxite': nation.bauxite, 'oil': nation.oil, 'uranium': nation.uranium,
                            'food': nation.food, 'steel': nation.steel, 'aluminum': nation.aluminum, 'gasoline': nation.gasoline, 'munitions': nation.munitions, 'money': nation.money}
        
        self.__projects = {'AC': nation.activity_center, 'AUP': nation.advanced_urban_planning, 'AEC': nation.advanced_engineering_corps, 'APE': nation.advanced_pirate_economy,
        'ALA': nation.arable_land_agency, 'AS': nation.arms_stockpile, 'BW': nation.bauxite_works, 'BDA': nation.bureau_of_domestic_affairs, 'CCE': nation.center_for_civil_engineering,
        'CRC': nation.clinical_research_center, 'EGR': nation.emergency_gasoline_reserve, 'FS': nation.fallout_shelter, 'GT': nation.green_technologies, 'GSA': nation.government_support_agency,
        'GS': nation.guiding_satellite, 'IA': nation.central_intelligence_agency, 'ITC': nation.international_trade_center, 'ID': nation.iron_dome, 'IW': nation.iron_works,
        'MARS': nation.mars_landing, 'MI': nation.mass_irrigation, 'MP': nation.metropolitan_planning, 'MS': nation.military_salvage, 'MLP': nation.missile_launch_pad,
        'MOON': nation.moon_landing, 'NLF': nation.nuclear_launch_facility, 'NRF': nation.nuclear_research_facility, 'PE': nation.pirate_economy, 'PB': nation.propaganda_bureau,
        'RI': nation.recycling_initiative, 'RDC': nation.research_and_development_center, 'SP': nation.space_program, 'SPTP': nation.specialized_police_training_program,
        'SS': nation.spy_satellite, 'SN': nation.surveillance_network, 'TS': nation.telecommunications_satellite, 'UEP': nation.uranium_enrichment_program, 'UP': nation.urban_planning,
        'VDS': nation.vital_defense_system}

        self.__cities = nation.cities

        self.__baseball_team = nation.baseball_team
        
        self.__troops['soldiers'] = {'total': nation.soldiers, 'casualties': nation.soldier_casualties, 'kills': nation.soldier_kills, 'max': nation.soldiers_today}
        self.__troops['tanks'] = {'total': nation.tanks, 'casualties': nation.tank_casualties, 'kills': nation.tank_kills, 'max': nation.tanks_today}
        self.__troops['aircraft'] = {'total': nation.aircraft, 'casualties': nation.aircraft_casualties, 'kills': nation.aircraft_kills, 'max': nation.aircraft_today}
        self.__troops['ships'] = {'total': nation.ships, 'casualties': nation.ship_casualties, 'kills': nation.ship_kills, 'max': nation.ships_today}
        self.__troops['spies'] = {'total': nation.spies, 'casualties': nation.spy_casualties, 'kills': nation.spy_kills, 'max': nation.spies_today}
        self.__troops['missiles'] = {'total': nation.missiles, 'casualties': nation.missile_casualties, 'kills': nation.missile_kills, 'max': nation.missiles_today}
        self.__troops['nukes'] = {'total': nation.nukes, 'casualties': nation.nuke_casualties, 'kills': nation.nuke_kills, 'max': nation.nukes_today}

        self.__war_policy = nation.war_policy
        self.__war_policy_turns = nation.war_policy_turns
        self.__wars_won = nation.wars_won
        self.__wars_lost = nation.wars_lost

        self.__offensive_wars_count = nation.offensive_wars_count
        self.__defensive_wars_count = nation.defensive_wars_count
        self.__wars = nation.wars

        self.__alliance = nation.alliance
        self.__aa_join_date = nation.alliance_join_date
        self.__aa_position = nation.alliance_position
        self.__aa_seniority = nation.alliance_seniority

    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def founded(self):
        return self.__founded
        
    def lastActive(self):
        return self.__last_active

    def discordUser(self):
        return self.__discord

    def flag(self):
        return self.__flag

    def population(self):
        return self.__population

    def nationScore(self):
        return self.__score

    def continent(self):
        return self.__continent

    def colorBlock(self):
        return self.__color_block

    def onVacation(self):
        return self.__vmode

    def stockpile(self):
        return self.__resources

    def projects(self):
        return self.__projects

    def specificProject(self, key):
        return self.__projects[key]

    def cities(self):
        return self.__cities
        
    def land(self):
        total = 0
        
        for city in self.__cities:
            total = total + city.land
        
        return total
        
    def infrastructure(self):
        total = 0
        
        for city in self.__cities:
            total = total + city.infrastructure

    def baseballTeam(self):
        return self.__baseball_team

    def troops(self):
        return self.__troops

    def soldiers(self):
        return self.__troops['soldiers']

    def tanks(self):
        return self.__troops['tanks']

    def aircraft(self):
        return self.__troops['aircraft']

    def ships(self):
        return self.__troops['ships']

    def spies(self):
        return self.__troops['spies']

    def missiles(self):
        return self.__troops['missiles']

    def nukes(self):
        return self.__troops['nukes']

    def warPolicy(self):
        return self.__war_policy

    def warPolicyTurns(self):
        return self.__war_policy_turns

    def warsWon(self):
        return self.__wars_won

    def warsLost(self):
        return self.__wars_lost

    def wars(self):
        return self.__wars

    def alliance(self):
        return self.__alliance

    def dateJoinedAlliance(self):
        return self.__aa_join_date

    def alliancePosition(self):
        return self.__aa_position

    def allianceSeniority(self):
        return self.__aa_seniority
        
    def stockpile(self):
        return self.__resources
