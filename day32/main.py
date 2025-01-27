import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()['iss_position']

longitude = data['longitude']
latitude = data['latitude']
iss_position = (longitude, latitude)