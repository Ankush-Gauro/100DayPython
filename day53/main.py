import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#links
google_forms_submit = "https://docs.google.com/forms/d/e/1FAIpQLScdIJSmtoLoElTrKbchK6QZAgManG-2SCuOt0n8HcdRweWgwA/viewform"
google_forms_reponses = "https://docs.google.com/forms/d/1jfL0NZtz7jiCKk7u-BnLRkFWYJH7pAUN9JKg-ngT52k/edit"
zillow = "https://appbrewery.github.io/Zillow-Clone/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(zillow, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

all_prices = soup.select(".PropertyCardWrapper span")
rental_price = [price.get_text().replace("/mo", "").split("+")[0] for price in all_prices if "$" in price.text]

all_address = soup.select(".StyledPropertyCardDataWrapper address")
rental_address = [address.get_text().replace(" | ", " ").strip() for address in all_address]

all_links = soup.select(".StyledPropertyCardDataWrapper a")
rental_links = [link["href"] for link in all_links]

#selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(rental_links)):
    driver.get(google_forms_submit)
    time.sleep(2)

    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent = driver.find_element(by=By.XPATH, value = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(rental_address[i])
    rent.send_keys(rental_price[i])
    link.send_keys(rental_links[i])
    submit.click()

