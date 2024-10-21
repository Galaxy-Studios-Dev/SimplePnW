class Bank:
    __kit = {}
    
    __name = ""
    __owner = {}
    __resources = {'stockpile': {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0, 'food': 0, 'steel': 0, 'aluminum': 0, 'gasoline': 0, 'munitions': 0, 'money': 0}, 'balance': {'coal': 0, 'iron': 0, 'lead': 0, 'bauxite': 0, 'oil': 0, 'uranium': 0, 'food': 0, 'steel': 0, 'aluminum': 0, 'gasoline': 0, 'munitions': 0, 'money': 0}}
    
    def __init__(self, simplepnw, owner):
        self.__kit = simplepnw
        
        self.__owner = owner
        self.__name = f"Bank of {owner.get().name()}"
        self.__resources['stockpile'] = self.__owner.get().stockpile()
        
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
        
    def specificResource(self, key):
        return self.__balance[key]
        
    def setBalance(self, value):
        self.__balance = value
        
    def save(self, path):
        data_manager = self.__kit.dataManager()
        desired_path = f"{data_manager.data_path}{path}"
        
        data_manager.save(desired_path, self.__resources)
        
    def setup(self, desired_path):
        data_manager = self.__kit.dataManager()
        
        self.__balance = data_manager.load(f"{desired_path}.json")