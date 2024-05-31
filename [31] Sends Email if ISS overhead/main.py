import time
import requests
from datetime import datetime, timezone
import smtplib

# --------------------------
MY_LAT = 19.218330  # Your latitude
MY_LONG = 72.978088  # Your longitude
MY_LAT_SAFE_RANGE = [(round(MY_LAT + number, 5)) for number in range(-5, 6)]
MY_LONG_SAFE_RANGE = [(round(MY_LONG + number, 5)) for number in range(-5, 6)]
MY_EMAIL = "vdoc.py@gmail.com"
MY_PASSWORD = "simpldev@098"
# --------------------------


# TODO:1 - Checking if the Satellite is near our location.
def satellite_near():
    """Checking if the current lat and lgt are in the range -5 to +5 from our location. """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if round(MY_LAT - 5, 6) <= iss_latitude <= round(MY_LAT + 5, 6) and \
            round(MY_LONG - 5, 6) <= iss_longitude <= round(MY_LONG + 5, 6):
        return True


# TODO:2 - Checking if its dark.
def is_dark():
    """Grabbing sunrise and sunset data for our location from another API endpoint."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    darkness_data = response.json()

    # Formatting the time from 12hr to 24hr and then splitting it twice to get only the hour part of the time.
    sunrise = int(darkness_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(darkness_data["results"]["sunset"].split("T")[1].split(":")[0])

    # Getting the utc time of our location as it will be synced with the output time of the above sunrise/sunset API.
    time_now = datetime.now(timezone.utc)
    hour = time_now.hour

    if hour >= sunset or hour <= sunrise:
        return True


# TODO:3 - Sending an email to ourselves if it's dark outside and satellite is near our location.
while True:
    time.sleep(60)
    if is_dark() and satellite_near():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:ISS overhead, LOOK UP!\n\n"
                                    "The ISS will be in your area soon, stay alert to witness it!", )
