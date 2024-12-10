from simplepnw.addon.dataman.sheets.Spreadsheet import Spreadsheet

class BuildSheet(Spreadsheet):
    def __init__(self, id):
        super().__init__("BUILD", id)

    def convertData(self):
        pass