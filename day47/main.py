import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find('span', class_='aok-offscreen').getText()
priceflt= float(price[2:])
print(priceflt)