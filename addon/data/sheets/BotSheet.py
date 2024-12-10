from simplepnw.addon.dataman.sheets.Spreadsheet import Spreadsheet

class BotSheet(Spreadsheet):
    def __init__(self, id):
        super().__init__("BOT", id)