import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "---"


class FlightSearch:

    def __init__(self):
        self.tequila_header = {
            "apikey": TEQUILA_API_KEY,
            }

    # We use this bit of code to find out the IATA codes for the cities in the gsheet.
    # We use the Tequila api to make this possible. This whole class is made to interact with the tequila api.
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        tequila_header = self.tequila_header
        tequila_parameters = {
            "term": city_name,
            "location_types": "city",
            "limit": 1,
        }
        response = requests.get(url=location_endpoint,
                                headers=tequila_header,
                                params=tequila_parameters)

        tequila_response = response.json()
        code = tequila_response["locations"][0]["code"]
        return code

    # This function will search for cheapest flights considering our choices which we mentioned in the main.py
    # This is from the tequila api.
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, ):
        tequila_header = self.tequila_header
        tequila_parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=tequila_header,
                                params=tequila_parameters)

        # If there are no flights available to the requested destination, this will let us know.
        # data = response.json()["data"][0]

        try:
            print(f"\nCITY: {destination_city_code}")
            data = response.json()["data"][0]
            route_len = len(response.json()["data"][0]["route"])
            print(f"Flight available with 0 stopover(s).")
            print(f"Total routes: {route_len}")

        except IndexError:
            print(f"No flights found with 0 stopover. Now trying with more stopover(s)...")
            for number in range(1, 6):
                tequila_parameters["max_stopovers"] = number

                response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                        headers=tequila_header,
                                        params=tequila_parameters)

                try:
                    data = response.json()["data"][0]
                    print(f"Flight available with {number} stopover(s).")
                    route_len = len(response.json()["data"][0]["route"])
                    print(f"No. of routes: {route_len}")

                except IndexError:
                    print(f"Couldn't find flight with {number} stopover(s).")
                    continue

                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["cityFrom"],
                    origin_airport=data["cityCodeFrom"],
                    destination_city=data["cityTo"],
                    destination_airport=data["cityCodeTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][route_len - 1]["local_arrival"].split("T")[0],
                    stop_overs=number,
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["cityCodeFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["cityCodeTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][route_len - 1]["local_arrival"].split("T")[0],
            )
            return flight_data
