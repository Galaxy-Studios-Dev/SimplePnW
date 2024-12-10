from deprecated import deprecated

from simplepnw.addon.Bank import Bank

class Nation:
    __query = {}
    __kit =  {}
    
    __warnings = {}
    
    __is_audited = True
    __can_loan = True
    __can_grant = True
    
    __bank = {}
    __build_plan = {}
    
    def __init__(self, simplepnw, nation_id):
        self.__kit = simplepnw
        self.__query = self.__kit.query('nation', nation_id)
        
        self.__bank = Bank(self)
        
    def get(self):
        return self.__query
    
    def canReceiveLoan(self):
        return self.__can_loan

    def canReceiveGrant(self):
        self.__can_grant

    def isAudited(self):
        return self.__is_audited

    def warning(self, key):
        return self.__warnings[key]

    def warnings(self):
        return self.__warnings

    @deprecated(reason="deprecated: v0.0.4\nuse Nation.warning(key: str)")
    def specificWarning(self, key):
        return self.__warnings[key]

    def bank(self):
        return self.__bank
        
    def buildPlan(self):
        return self.__build_plan

    @deprecated(reason="")
    def cities(self):
        for data in self.get().cities():
            city = City(data.name, data.infrastructure, data.land)
            city.setBuilds({'coal': data.coal_power, 'oil': data.oil_power, 'nuclear': data.nuclear_power, 'wind': data.wind_power},
                           {'coal': data.coal_mine, 'iron': data.iron_mine, 'lead': data.lead_mine, 'bauxite': data.bauxite_mine, 'oil': data.oil_well, 'uranium': data.uranium_mine, 'food': data.farm},
                           {'steel': data.steel_mill, 'aluminum': data.aluminum_refinery, 'gasoline': data.oil_refinery, 'munitions': data.munitions_factory},
                           {'police': data.police_station, 'hospitals': data.hospital, 'recycling': data.recycling_center, 'subways': data.subway},
                           {'markets': data.supermarket, 'banks': data.bank, 'malls': data.shopping_mall, 'stadiums': data.stadium},
                           {'barracks': data.barracks, 'factories': data.factory, 'hangars': data.hangar, 'drydocks': data.drydock})

            self.__cities[data.name] = city

        return self.__cities

    @deprecated(reason="")
    def checkMMR(self, required):
        cities = self.get().cities()
        
        audit = {}
        
        for city in cities:
            if city.barracks >= required['barracks'] and city.factory >= required['factories'] and city.hangar >= required['hangars'] and city.drydock >= required['drydocks']:
                audit[city.name] = "passed"
            else:
                audit[city.name] = f"{city.barracks}{city.factory}{city.hangar}{city.drydock}"
                
        return audit
    
    def setCanLoan(self, value: bool):
        self.__can_loan = value

    def setCanGrant(self, value: bool):
        self.__can_grant = value
        
    def setIsAudited(self, value: bool):
        self.__is_audited = value
        
    def setBuildPlan(self, build_plan):
        self.__build_plan = build_plan
        
    def requery(self):
        self.__query = self.__kit.query("nation", self.__query.id())
