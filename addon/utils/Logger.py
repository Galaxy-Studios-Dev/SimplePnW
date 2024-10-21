from datetime import datetime

class Logger:
    __kit = {}
    __name = ""
    
    __date = ""
    __time = ""
    
    __log_header = ""
    
    def __init__(self, simplepnw, name):
        self.__kit = simplepnw
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
        data_manager = self.__kit.dataManager()
        self.formatTime(datetime.now())
        
        with open(f"{data_manager.log_path}{self.__date}.log", 'a+') as log:
            log.write(f"{self.__log_header}{content}\n")