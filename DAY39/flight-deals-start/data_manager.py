import requests
import os 
from pprint import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()



SHEETY_GET = "https://api.sheety.co/5cd4f795c01ecc865b2ae32ccd698ea1/copyOfFlightDeals/prices"
SHEETY_PUT = "https://api.sheety.co/5cd4f795c01ecc865b2ae32ccd698ea1/copyOfFlightDeals/prices/"
sheety_USERNAME = "Agauro"
sheety_PASSWORD = os.getenv("PASSWORD")

class DataManager():
    def __init__(self):
        self._user = sheety_USERNAME
        self._password = sheety_PASSWORD
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET, auth=(sheety_USERNAME, sheety_PASSWORD))
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    'iataCode' : city['iataCode']
                }
            }
            response = requests.put(
                url = f"{SHEETY_PUT}/{city['id']}",
                json = new_data,
                auth = (sheety_USERNAME, sheety_PASSWORD)
            )



