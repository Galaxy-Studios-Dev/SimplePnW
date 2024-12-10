import traceback

import requests
from requests.exceptions import ConnectionError

import pnwkit

from simplepnw.addon.dataman.DataManager import DataManager
from simplepnw.addon.dataman.SpreadsheetManager import SpreadsheetManager
from simplepnw.addon.utils.Logger import Logger

from simplepnw.queries.NationQuery import NationQuery
from simplepnw.queries.AllianceQuery import AllianceQuery
from simplepnw.queries.MarketPriceQuery import MarketPriceQuery

class SimplePnW:
    __default_path = 'https://api.politicsandwar.com/graphql?api_key='
    __nations_api_url = 'https://politicsandwar.com/api/nations/?key='
    __token = ''
    __pnwkit = ""
    
    __data_manager = {}
    __logger = {}

    def __init__(self, token, files_enabled, sheets_enabled, api_key="", main_path="", sheets={}):
        self.__token = token
        self.__pnwkit = pnwkit.QueryKit(self.__token)
        
        if files_enabled:
            print("Enabling DataManager....")
            self.__data_manager = DataManager(main_path)
            self.__logger = Logger(self, 'simplepnw')
            
            self.__logger.log("DataManager has been enabled successfully!")
        elif sheets_enabled:
            print("Enabling Spreadsheet Manager....")
            self.__spreadsheet_manager = SpreadsheetManager(api_key, sheets)
        else:
            print("Datamanagement has been disabled... Set files_enabled or sheets_enabled to True...")
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
        elif given_type == "prices":
            return MarketPriceQuery(self, given_id)
        elif given_type == "nations":
            try:
                nations_data = requests.get(f'{self.__nations_api_url}{self.__token}').json()
                return nations_data["nations"]
            except json.decoder.JSONDecodeError:
                self.__logger.log("JSON Decode Error while connecting to the nations api! The recruiter will try again later...")
            except ConnectionError:
                self.__logger.log("Connection Error while connecting to the nations api!\nIs the server down? The recruiter will try again later...")
            except KeyError:
                self.__logger.log("There was a problem with the given api key! Are you out of api calls?\nThe recruiter will try again later...")
            except:
                self.__logger.log("There was an issue connecting to the api! The recruiter will try again later...")
            return None

    def mutate(self, given_type):
        if given_type == "withdraw":
            pass
        elif given_type == "deposit":
            pass

    def setToken(self, value):
        self.__token = value