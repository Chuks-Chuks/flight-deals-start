from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()
sheet_data = data.prices

for iata_code in sheet_data:
    city = FlightSearch(iata_code['city'])
    if iata_code["iataCode"] == "":
        iata_code["iataCode"] = city.response
        data.put(iata_code)
    else:
        flight_data = FlightData(iata_code["iataCode"])
        check_price = NotificationManager(flight_data.price,
                                          iata_code['lowestPrice'],
                                          flight_data.stripped_date,
                                          flight_data.six_months,
                                          flight_data.city_from,
                                          flight_data.city_to
                                          )

