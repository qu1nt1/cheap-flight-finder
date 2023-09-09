from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


destinations = {}
message = "Price alert:\n"

data_to_search = DataManager()
flight_data = data_to_search.return_row()

for n in range(0, len(flight_data["prices"])):
    iata_code = flight_data["prices"][n]["iataCode"]
    lowest_price = flight_data["prices"][n]["lowestPrice"]
    flightsearch = FlightSearch(iata_code)
    try:
        lowest_price, best_data = flightsearch.search_best_prices(lowest_price)
    except KeyError:
        print(f"INVALID IATA CODE: {iata_code}")
        lowest_price = None
    if lowest_price != None:
        destinations[iata_code] = lowest_price, best_data

for iata in destinations:
    for country in flight_data["prices"]:
        if iata == country["iataCode"]:
            message += f"R${destinations[iata][0]} to fly to {country['city']} on {destinations[iata][1].split('T')[0]}\n"


message_menager = NotificationManager()
message_menager.send_message(message)
