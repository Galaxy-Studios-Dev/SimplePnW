from simplepnw.addon.dataman.sheets.Spreadsheet import Spreadsheet

class BankSheet(Spreadsheet):
    def __init__(self, id):
        super().__init__("BANK", id)

    def convertData(self):
        pass