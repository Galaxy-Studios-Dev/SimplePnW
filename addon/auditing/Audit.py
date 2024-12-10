class Audit:
    __name = ""
    __status = False

    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def status(self):
        return self.__status

    def setName(self, value: str):
        self.__name = value

    def setStatus(self, value: bool):
        self.__status = value

    def run(self):
        print("Starting Audit....")
        print("Checking the name of the audit....")
        if self.__name == "Activity Audit":
            print(f"Audit Type: {self.__name}...Continuing...")
        elif self.__name == "Build Audit":
            print(f"Audit Type: {self.__name}...Continuing...")