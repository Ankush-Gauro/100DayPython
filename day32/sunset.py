import requests
from datetime import datetime
import smtplib
import time

my_email = "ajnight124@gmail.com"
password = "123456"
MY_LAT = 43.795043
MY_LNG = -79.349182

def is_issoverhead():
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    data_iss = response_iss.json()['iss_position']

    longitude = data_iss['longitude']
    latitude = data_iss['latitude']
    if MY_LNG - 5 <= longitude <= MY_LNG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True


def is_night():
    location = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=location)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_issoverhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="agauro@myseneca.ca",
                msg="Subject:Look Up\n\nThe ISS is above you in the sky."
            )

#Run everyday on cloud using pythonanywhere.com