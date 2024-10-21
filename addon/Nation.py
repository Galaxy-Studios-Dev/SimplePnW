from simplepnw.addon.Bank import Bank

class Nation:
    __query = {}
    __kit =  {}
    
    __discord = {}
    
    __bank = {}
    
    def __init__(self, simplepnw, nation_id):
        self.__kit = simplepnw
        self.__query = self.__kit.query('nation', nation_id)
        
        self.__bank = Bank(self.__kit, self)
        
    def get(self):
        return self.__query
        
    def discord(self):
        return self.__discord
        
    def discordId(self):
        return self.__discord.id
        
    def bank(self):
        return self.__bank
        
    def setDiscord(self, discord_user):
        self.__discord = discord_user
