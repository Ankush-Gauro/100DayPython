from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
sheet = data_manager.get_destination_data()

flight_search = FlightSearch()

if sheet[0]['iataCode'] == '':
    for city in sheet:
        city['iataCode'] = flight_search.get_destination_code(city['city'])

    data_manager.destination_data = sheet
    data_manager.update_destination_code()