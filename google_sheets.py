
import gspread
import pandas as pd
import toml
from google.oauth2.service_account import Credentials

# Function to get data from Google Sheet
def get_data_from_sheet(sheet_name):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds_dict = toml.load(".streamlit/secrets.toml")['gcp_credentials']
        creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open(sheet_name).worksheet("wins_losses")
        data = sheet.get_all_records()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to get match history from Google Sheet
def get_match_history_from_sheet(sheet_name):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds_dict = toml.load(".streamlit/secrets.toml")['gcp_credentials']
        creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open(sheet_name).worksheet("matches")
        data = sheet.get_all_records()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
