import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
API = os.getenv("API")

SHEETY = os.getenv("SHEETY")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

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
result = response.json()

today_date = datetime.now().strftime("%Y-%m-%d")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout" : {
            "date" : today_date,
             "time": now_time,
             "exercise": exercise['name'].title(),
             "duration" : exercise['duration_min'],
             "calories" : exercise['nf_calories']
        }
    }
    sheet_response = requests.post(url=SHEETY, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    print(sheet_response.text)