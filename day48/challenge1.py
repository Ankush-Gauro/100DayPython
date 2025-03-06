from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")
dates = []
names = []
event_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for i in event_date:
    dates.append(i.text)

for i in event_name:
    names.append(i.text)

dic = dict(zip(dates, names))
print(dic)