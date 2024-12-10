types = ["BOT", "MEMBERS", "BUILDS", "BANK", "CBANK"]

class SpreadsheetManager:
    __bot_data = {}
    __member_sheets = {}
    __build_sheets = {}
    __bank_sheets = {}
    __coalition_bank_sheets = {}

    def __init__(self, api_key: str, spreadsheets: dict):
        for key in spreadsheets.keys():
            spreadsheet = spreadsheets[key]
            upper = spreadsheet.type().upper()
            spreadsheet.setApiKey(api_key)

            if upper == types[0]:
                self.__bot_data = spreadsheet
            elif upper == types[1]:
                self.__member_sheets[key] = spreadsheet
            elif upper == types[2]:
                self.__build_sheets[key] = spreadsheet
            elif upper == types[3]:
                self.__bank_sheets[key] = spreadsheet
            elif upper == types[4]:
                self.__coalition_bank_sheets[key] = spreadsheet

    def botSettings(self):
        return self.__bot_settings

    def setBotSettings(self):
        pass

    def createSheet(self, type, id):
        if type == types[0]:
            return BotSheet(id)
        elif type == types[1]:
            return MemberSheet(id)
        elif type == types[2]:
            return BuildPlanSheet(id)
        elif type == types[3]:
            return BankSheet(id, False)
        elif type == types[4]:
            return BankSheet(id, True)