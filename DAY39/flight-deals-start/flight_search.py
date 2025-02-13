import os
import requests
class FlightSearch:

    def __init__(self):
        self._apikey = os.getenv('apadeusApi')
        self._apisecret =  os.getenv('amadeusKey')
        self._token = self._get_new_token()


    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._apikey,
            'client_secret': self._apisecret
        }
        response = requests.post(url='https://test.api.amadeus.com/v1/security/oauth2/token', headers=header, data=body)

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    
        
    
    def get_destination_code(self, city):
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url="https://api.amadeus.net/v1/reference-data/locations/cities",
            headers=headers,
            params=query
        )
        
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code