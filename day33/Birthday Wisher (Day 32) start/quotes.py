import datetime as dt
import smtplib
import random 

my_email = "ajnight124@gmail.com"
password = "ajnight124"

with open ("day33\Birthday Wisher (Day 32) start\quotes.txt") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)

now = dt.datetime.now()
if now.weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="agauro@myseneca.ca", msg=f"Subject:Monday Motivation\n\n{quote}")
