from simplepnw.addon.Bank import Bank

class Coalition:
    __leader = {}
    __name = ""
    
    __members = {}
    __bank = {}
    
    def __init__(self, name, alliance):
        self.__name = name
        self.__leader = alliance

        self.__bank = Bank(alliance)
        resources = {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0,
                     'food': 0, 'steel': 0, 'aluminum': 0, 'gasoline': 0, 'munitions': 0, 'money': 0}

        self.__bank.setBalance(resources)

    def name(self):
        return self.__name
        
    def leader(self):
        return self.__leader
        
    def members(self):
        return self.__members
        
    def bank(self):
        return self.__bank
    
    def transfer(self, value):
        self.__leader = value
    
    def addMember(self, key: str, value):
        self.__member[key] = value

    def setMembers(self, alliances: dict):
        self.__members = alliances