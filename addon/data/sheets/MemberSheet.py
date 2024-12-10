from simplepnw.addon.dataman.sheets.Spreadsheet import Spreadsheet

class MemberSheet(Spreadsheet):
    def __init__(self, id):
        super().__init__("MEMBER", id)

    def convertData(self):
        pass