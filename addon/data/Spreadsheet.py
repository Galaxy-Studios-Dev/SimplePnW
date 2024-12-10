from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

from simplepnw.addon.utils.Logger import Logger

class Spreadsheet:
	__logger = Logger("simplepnw", "")

	__type = ""
	__id = ""
	__api_key = ""

	__ranges = {}

	def __init__(self, type, id):
		self.__type = type
		self.__id = id

	def type(self):
		return self.__type

	def id(self):
		return self.__id

	def range(self, key):
		return self.__ranges[key]

	def ranges(self):
		return self.__ranges

	def apiKey(self):
		return self.__api_key

	def authenticate(self):
		return build('sheets', 'v4', developerKey=self.__api_key).spreadsheets()

	def addRange(self, key: str, value: str):
		self.__ranges[key] = value

	def removeRange(self, key: str):
		if key in self.__ranges.keys():
			self.__ranges.pop(key)
		else:
			print("Key doesn't exist...")

	def setApiKey(self, value):
		self.__api_key = value

	def data(self, data_range):
		try:
			sheet = self.authenticate()

			result = (
				sheet.values()
				.get(spreadsheetId=self.__id, range=data_range)
				.execute()
			)
			values = result.get("values", [])

			if not values:
				print("No data found.")
				return

			return values
		except HttpError as err:
			print(err)

	def writeData(self, data_range, data):
		worksheet.insert_row(data, len(self.data(data_range)) - 1)

	def appendData(self, data_range, data):
		self.authenticate().values().append(spreadsheetId=self.__id, range=data_range,
											valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS",
											body={"values":data})