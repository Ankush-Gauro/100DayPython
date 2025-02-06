import requests

APP_ID = "8fa0ada5"
API_KEY = "17416f1aa78518b07905bfde83741186"
API = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("What exercises did you do today?")

headers = {
    'x-app-id' : APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query' : text,
    "weight_kg": 61,
    "height_cm": 180,
    "age": 20
}

response = requests.post(url=API, json=parameters, headers=headers)
print(response.json())