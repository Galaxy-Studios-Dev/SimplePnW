class Bank:
    __kit = {}
    
    __name = ""
    __owner = {}
    __resources = {'stockpile': {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0, 'food': 0, 'steel': 0, 'aluminum': 0, 'gasoline': 0, 'munitions': 0, 'money': 0}, 'balance': {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0, 'food': 0, 'steel': 0, 'aluminum': 0, 'gasoline': 0, 'munitions': 0, 'money': 0}}
    
    def __init__(self, owner):
        
        self.__owner = owner
        self.__name = f"Bank of {owner.get().name()}"
        
    def name(self):
        return self.__name
        
    def owner(self):
        return self.__owner
        
    def resources(self):
        return self.__resources
        
    def balance(self):
        return self.__resources['balance']
        
    def stockpile(self):
        return self.__resources['stockpile']
        
    def setName(self, value: str):
        self.__name = value
        
    def transfer(self, value):
        self.__owner = value
        
    def setStockpile(self, value: dict):
        self.__resources['stockpile'] = value
        
    def setBalance(self, value: dict):
        self.__resources['balance'] = value
        
    def save(self, path):
        data_manager = self.__kit.dataManager()
        data_manager.save(path, self.__resources)
        
    def setup(self, desired_path):
        data_manager = self.__kit.dataManager()
        
        self.__balance = data_manager.load(f"{desired_path}.json")