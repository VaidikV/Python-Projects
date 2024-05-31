import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone

# ----------------------------------
# google sheet link - https://docs.google.com/spreadsheets/d/1iiKexJk4XyaTYvFOxhtzgi0k1qkf7mwOfa8sDJ9X7H0/edit#gid=0
load_dotenv("D:/Python/EnvironmentVariables/.env.txt")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_APPID = os.getenv("NUTRITIONX_APPID")
NUTRI_APIKEY = os.getenv("NUTRITIONX_APIKEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
# ----------------------------------

# Date and time
tz = timezone("Asia/Kolkata")
TODAY_DATE = datetime.now(tz).strftime("%d/%m/%Y")
CURRENT_TIME = datetime.now(tz).time().strftime("%X")

# Fetching exercise data using natural language engine from nutritionix.
headers = {
    "x-app-id": NUTRI_APPID,
    "x-app-key": NUTRI_APIKEY,
}

parameters = {
    "query": input("Tell me which exercises you did:\n"),
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 165,
    "age": 18
}

response = requests.post(url=NUTRI_ENDPOINT, json=parameters, headers=headers)
nutrinixai_data = response.json()

# Inputting the exercise data to a google form using sheety.
for exercise in nutrinixai_data["exercises"]:
    sheety_header = {
        "Authorization": SHEETY_AUTH,
        "Content-Type": "application/json",
    }
    sheety_parameters = {
        "workout": {
            "date": TODAY_DATE,
            "time": CURRENT_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_header)
    sheety_response.raise_for_status()
