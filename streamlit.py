from oauth2client.service_account import ServiceAccountCredentials
import gspread

# defining globals
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
  'credentials.json', scope
  )

client = gspread.authorize(creds)

# opening the google sheet
sheet = client.open_by_url(
  url="https://docs.google.com/spreadsheets/d/104xwMd-oVJp4pYCFqUtMmDYDaCxU363U3mA9BYDvdM8/edit?usp=sharing"
  )

# accessing the specific worksheet by index 
# if index is left blank the first sheet will be read
worksheet = sheet.get_worksheet(index=0)


# defining a function to read all records from the worksheet
def get_all_records(worksheet=worksheet):
    records = worksheet.get_all_records()

    return records
