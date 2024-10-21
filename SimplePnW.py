import requests
import pnwkit

from simplepnw.addon.utils.DataManager import DataManager
from simplepnw.addon.utils.Logger import Logger

from simplepnw.queries.AllianceQuery import AllianceQuery
from simplepnw.queries.NationQuery import NationQuery


class SimplePnW:
    __default_path = 'https://api.politicsandwar.com/graphql?api_key='
    __token = ''
    __pnwkit = ""
    
    __data_manager = {}
    __logger = {}

    def __init__(self, token, main_path, data_enabled):
        self.__token = token
        self.__pnwkit = pnwkit.QueryKit(self.__token)
        
        if data_enabled:
            print("Enabling DataManager....")
            self.__data_manager = DataManager(main_path)
            self.__logger = Logger(self, 'simplepnw')
            
            self.__logger.log("DataManager has been enabled successfully!")
        else:
            print("DataManager has been disabled.... Set data_enabled to True to enable DataManager!")
            self.__data_manager = None

    def token(self):
        return self.__token

    def apiPath(self):
        return self.__default_path

    def legacyKit(self):
        return self.__pnwkit
        
    def dataManager(self):
        return self.__data_manager
        
    def devLogger(self):
        return self.__logger

    def query(self, given_type, given_id):
        if given_type == "nation":
            return NationQuery(self, given_id)
        elif given_type == "alliance":
            return AllianceQuery(self, given_id)

    def mutate(self, given_type):
        if given_type == "withdraw":
            pass
        elif given_type == "deposit":
            pass
