from simplepnw.addon.Nation import Nation

from simplepnw.addon.nation.City import City
from simplepnw.addon.Bank import Bank

class DiscordNation(Nation):
    __discord = {}

    def __init__(self, simplepnw, nation_id: int):
        super().__init__(simplepnw, nation_id)

    def discord(self):
        return self.__discord
        
    def discordId(self):
        return self.__discord.id
        
    def setDiscord(self, discord_user):
        self.__discord = discord_user
