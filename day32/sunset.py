import requests
from datetime import datetime

location = {
    'lat': 43.795043,
    'lng': -79.349182,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=location)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now().hour
print(time_now)