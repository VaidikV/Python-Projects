import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from twilio.rest import Client

# -------------------------------------------------------
load_dotenv("D:/Python/EnvironmentVariables/.env.txt")
AV_stock_endpoint = "https://www.alphavantage.co/query"
NEWS_API_endpoint = "https://newsapi.org/v2/everything"
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
AV_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_api_key = os.getenv("NEWS_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
# -------------------------------------------------------

# Fetching yesterday's and day before yesterday's date
time_now = datetime.now()
today_date = time_now.date()
yesterdays_date = today_date - timedelta(days=1)
day_before_yest_date = today_date - timedelta(days=2)

# storing the detail (increase in price/decrease) and value (% increase/decrease) in this dictionary so that the data
# can be used anywhere in the code.
detail_value = {
    "detail": "",
    "value": 0,
}


def get_news_and_send_message():
    parameters = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_api_key,
    }
    news_response = requests.get(url=NEWS_API_endpoint, params=parameters)
    news_data = news_response.json()

    title_1 = news_data["articles"][0]["title"]
    description_1 = news_data["articles"][0]["description"]

    # title_2 = news_data["articles"][1]["title"]
    # description_2 = news_data["articles"][1]["description"]
    #
    # title_3 = news_data["articles"][2]["title"]
    # description_3 = news_data["articles"][2]["description"]

    formatted_msg = f"{COMPANY_NAME}: {detail_value['detail']}{detail_value['value']}%"

    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
            body=f"\n{formatted_msg}\n\nHeadline: {title_1}\n\nBrief: {description_1}",
            from_='+16193042608',
            to='+919029783838'
        )
    print(message.status)


def stocks():
    # Setting the parameters for the api endpoint.
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_api_key,
    }

    stock_response = requests.get(url=AV_stock_endpoint, params=parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]

    data_list = [value for (key, value) in stock_data.items()]
    yest_stocks = data_list[0]
    day_before_yest_stocks = data_list[1]

    yest_stock_close = float(yest_stocks["4. close"])
    day_before_yest_stock_close = float(day_before_yest_stocks["4. close"])
    # yest_stock_close = 900
    # day_before_yest_stock_close = 948

    print(f"YCSP: {yest_stock_close}")
    print(f"DBYCSP: {day_before_yest_stock_close}")

    if yest_stock_close > day_before_yest_stock_close:
        # Here the "increase" var is the difference between the two stock prices. This is used to further calculate
        # the % increase/decrease between the two stocks.
        increase = yest_stock_close - day_before_yest_stock_close
        percent_increase = (increase / day_before_yest_stock_close) * 100
        # setting the "detail" and "value" keys of the detail_value dictionary to their respective values. check below
        detail_value["detail"] = "🔺"
        detail_value["value"] = round(percent_increase)  # rounding off the %no
    else:
        increase = day_before_yest_stock_close - yest_stock_close
        percent_decrease = (increase / yest_stock_close) * 100
        detail_value["detail"] = "🔻"
        detail_value["value"] = round(percent_decrease)

    test = f"{COMPANY_NAME}: {detail_value['detail']}{detail_value['value']}%"
    print(test)

    if detail_value['value'] >= 5:
        print("Message sent")
        get_news_and_send_message()
    else:
        print("Message not sent")


stocks()
