class Warning:
    __reason = ""
    __date = ""
    __falloff_date = ""

    def __init__(self, reason, date):
        self.__reason = reason
        self.__date = date

    def reason(self):
        return self.__reason

    def date(self):
        return self.__date

    def falloffDate(self):
        return self.__falloff_date