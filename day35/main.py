import requests
from twilio.rest import Client

api_key = "5df6e68e86cfcd3141707fd2471xxxx"
account_sid = "AC0c505437c7563224d84fe0d91150xxxx"
auto_token = "9bb0620a92781e4dade501b24f5xxxxx"



will_rain = False

weather_params = {
    "lat" : 43.795043,
    "lon" : -79.349182,
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()
for item in weather_data["list"]:
    condition_code = item["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auto_token)
    message = client.messages \
        .create(
            body="It's going to rain today!", from_='whatsapp:+1415523xxxx', to='whatsapp:+xxxxx'
        )
    print(message.status)