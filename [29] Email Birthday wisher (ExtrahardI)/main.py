import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "vdoc.py@gmail.com"
MY_PASSWORD = "simpldev@098"

PLACEHOLDER = "[NAME]"
birthday_today_details = []

# TODO:1 - Fetching today's month and date.
today_details = dt.datetime.now()  # here now() is the method and below are its attribute
current_month = today_details.month  # month is the attribute
current_day = today_details.day

# TODO:2 - Reading csv and checking if today is someone's birthday. Then adding their name to the final list.
birthday_dataframe = pandas.read_csv("birthdays.csv")

for (index, row) in birthday_dataframe.iterrows():
    if row.month == current_month and row.day == current_day:
        details = {"Name": row["name"],
                   "Email": row["email"]}
        birthday_today_details.append(details)

# TODO:3 - Structuring the email for the birthday person
with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
    letter_contents = letter.read()
    for person in birthday_today_details:
        name = person["Name"]
        email = person["Email"]
        edited_letter = letter_contents.replace(PLACEHOLDER, name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}!\n\n{edited_letter}"
            )
# --- CONDITIONS
# Extra Hard Starting Project

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
