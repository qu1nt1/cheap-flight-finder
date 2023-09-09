from flight_data import FlightData
import requests
import os

class FlightSearch:

        def __init__(self, iata):
            self.tequila_endpoint = "https://api.tequila.kiwi.com/v2/search?"
            self.tequila_apikey = os.environ.get("TEQUILA_APIKEY")
            self.tequila_header = {
                "accept": "application/json",
                "apikey": self.tequila_apikey
            }

            self.flightdata = FlightData()

            self.tequila_params = {
                "fly_from": "GRU",
                "fly_to": iata,
                "date_from": self.flightdata.date,
                "date_to": self.flightdata.next_six_months_date(),
                "curr": "BRL",
            }

            self.response = requests.get(url=self.tequila_endpoint, params=self.tequila_params, headers=self.tequila_header)
            self.avaliable_dates = self.response.json()

        def search_best_prices(self, lowest_price):
            best_data = ""
            initial_lowest = lowest_price
            for n in range(0, len(self.avaliable_dates["data"])):
                if self.avaliable_dates["data"][n]["price"] < lowest_price:
                    lowest_price = self.avaliable_dates["data"][n]["price"]
                    best_data = self.avaliable_dates["data"][n]["local_departure"]
                if lowest_price == initial_lowest:
                    return None, None
            return lowest_price, best_data

