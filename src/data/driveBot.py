from dotenv import load_dotenv
import gspread
import pandas as pd
import os

load_dotenv()

class driveBot:
    def __init__(self):
        self.gc = gspread.service_account(filename="credentials.json")
    
    def get_data(self):
        link_google_sheet = os.getenv("LINK_SHEET")
        sh = self.gc.open_by_key(link_google_sheet)
        worksheet = sh.sheet1
        df = pd.DataFrame(worksheet.get_all_records())
        return df
        
        