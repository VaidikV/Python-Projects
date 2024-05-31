import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("D:/Python/EnvironmentVariables/.env.txt")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("OWM_API_KEY")
twilio_account_sid = "---"
twilio_auth_token = "---"
MY_LAT = 19.218330
MY_LON = 72.978088

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "units": "metric",
    "exclude": "current,minutely,daily,alerts",
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

next_12_hours = []

for hour in range(0, 12):
    weather_id = data["hourly"][hour]["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        next_12_hours.append("rains_appear")

if "rains_appear" in next_12_hours:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages\
        .create(
            body="It's going to rain today. Don't forget to take an umbrella ☂ with you.",
            from_='+2039483949',
            to='+911234567890'
        )
    print(message.status)


