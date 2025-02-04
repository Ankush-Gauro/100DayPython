import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api = "9XWYHJ4GQZQ0QWQB"
news_api = "d5154e76da674fcc9021b1c661432cdb"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "AC0c505437c7563224d84fe0d91150xxxx"
auto_token = "9bb0620a92781e4dade501b24f5xxxxx"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stocks_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : stock_api
}

response = requests.get(STOCK_ENDPOINT, params=stocks_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (date, value) in data.items()]
yesterday_closing = data_list[0]['4. close']

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_closing = data_list[1]['4. close']

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.

diff = (float(yesterday_closing) - float(day_before_yesterday_closing))
up_down = None
if diff > 0:
    up_down = "📈"
else:
    up_down = "📉"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = round(diff / float(yesterday_closing)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

#if diff_percent > 5:
#   print("Get News")

 ## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(diff_percent) > 5:
    news_params = {
        'apiKey' : news_api,
        'qInTitle' :  COMPANY_NAME

    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles'][:3]
    print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.


## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number. 


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f"{STOCK_NAME} : {up_down} {diff_percent}%\nHeadline:  {article['title']} \n Description: {article['description']}" for article in articles]

#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(account_sid, auto_token)

for article in formatted_articles:
    message = client.messages.create(
        body = article,
        from_ = 'whatsapp:+1415523xxxx',
        to = 'whatsapp:+xxxxx'
    )

