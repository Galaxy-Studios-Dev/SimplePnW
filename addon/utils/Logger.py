import os.path
from datetime import datetime

class Logger:
    __kit = {}

    __path = ""

    __name = ""
    
    __date = ""
    __time = ""
    
    __log_header = ""
    
    def __init__(self, name, path):

        if path == "" and name != "simplepnw" or name == "":
            print("Invalid path given... Prevented throwing error...")
            return None

        if name == "simplepnw":
            self.__path = f"{os.path.expanduser('~')}simplepnw/logs/"
        else:
            self.__path = f"{os.path.expanduser('~')}{path}logs/"

        print(self.__path)
        self.__name = name
        date = datetime.now()

        self.formatTime(date)
        
        if self.__name == "simplepnw":
            self.__log_header = self.setLogHeader('simplepnw')
            
        else:
            self.__log_header = self.setLogHeader(self.__name)
            
    def setLogHeader(self, value):
        self.__log_header = f"{self.__time}|{value}| "
        
    def formatTime(self, date):
        self.__date = f"{date.month}-{date.day}-{date.year}"
        self.__time = f"{date.hour}:{date.minute}:{date.second}"
        self.__log_header = self.setLogHeader(self.__name)
        
    def log(self, content):
        self.formatTime(datetime.now())
        
        with open(f"{self.__path}{self.__date}.log", 'a+') as log:
            log.write(f"{self.__log_header}{content}\n")