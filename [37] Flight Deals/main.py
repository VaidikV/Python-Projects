from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_DATA = "BOM"

# IATA Code populator
for row in sheet_data:
    if row["IATA Code"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        row["IATA Code"] = flight_search.get_destination_code(row["City"])

# We updated the sheet_data in the above code. Now we are making sure that the destination data
# is the same as the sheet_data and then finally updating the google sheet with IATA codes.
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# Finding out today's date and date of the day six months from now.
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(30 * 6))
# print(tomorrow, six_months_from_today)

# Finding cheapest flights from our location to the location mentioned in the google sheet.
# Also including the timeframe which we made above.
for row in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_DATA,
        row["IATA Code"],
        from_time=tomorrow,
        to_time=six_months_from_today,
    )

    url = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}" \
          f".{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

    if flight is None:
        continue  # skip the below code and start the loop again.

    if flight.price < row["Lowest Price"]:
        print(f"Sending message for {flight.destination_city}!")

        message = f"💸 Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}.\n \n" \
                  f"📅 From {flight.out_date} to {flight.return_date}.\n \n📍 This flight has {flight.stop_overs}" \
                  f" stopover(s).\n \n🔗 Link to buy the tickets:\n" \
                  f"{url}"

        # notification_manager.send_message(message)
        notification_manager.send_emails(message)
    else:
        print(f"Flight price for {flight.destination_city} (₹{flight.price}) is not lower than your "
              f"Lowest price preference (₹{row['Lowest Price']}). No messages sent.")





