import gspread
from oauth2client.service_account import ServiceAccountCredentials

# -----------------------------
google_sheet_link = "https://docs.google.com/spreadsheets/d/1CNeG6gIlU6pfV78XvWQRiDyRuKgInRAR9C59yFdwf5o/edit#gid=0"
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
prices = client.open("Flight Deals").get_worksheet(0)  # Open the specific worksheet
users = client.open("Flight Deals").get_worksheet(1)
# -----------------------------


class DataManager:

    def __init__(self):
        self.destination_data = []
        self.user_data = []

    def get_destination_data(self):
        self.destination_data = prices.get_all_records()
        return self.destination_data

    def get_user_data(self):
        self.user_data = users.get_all_records()
        return self.user_data

    def update_destination_codes(self):
        for row in self.destination_data:
            current_row = self.destination_data.index(row) + 2
            prices.update_cell(current_row, 2, row["IATA Code"])
