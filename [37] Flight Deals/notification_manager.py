import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib
from data_manager import DataManager

load_dotenv("D:/Python/EnvironmentVariables/.env.txt")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NO = os.getenv("TWILIO_FROM_NO")
MY_GMAIL = os.getenv("MY_GMAIL")
MY_GPASSWORD = os.getenv("MY_GPASSWORD")

data_manager = DataManager()
user_data = data_manager.get_user_data()


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        """ This class is responsible for sending notifications with the deal flight details. """

        message = self.client.messages \
            .create(
                body=message,
                from_=TWILIO_FROM_NO,
                to='+919029783838'
            )

        print(message.status)

    def send_emails(self, message):
        for row in user_data:
            email = row["Email"]
            name = row["First Name"]

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_GMAIL, password=MY_GPASSWORD)
                connection.sendmail(
                    from_addr=MY_GMAIL,
                    to_addrs=email,
                    msg=f"Subject: ✈ Hello, {name}. Here's a great flight deal!\n\n{message}".encode("utf-8")
                )
