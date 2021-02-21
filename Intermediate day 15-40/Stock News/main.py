import requests
from twilio.rest import Client
import os

# 6:00 UTC, run export env SID={account_sid};export env AUTH={auth_token}; python main.py
account_sid = os.environ.get()
auth_token = os.environ.get()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "http://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']
stock_data_list = [
    value for (key, value) in stock_data.items()
]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

up_down = None

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_prec = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_prec) > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']

    first_three_articles = news_data[:3]

    article = [
        f"{STOCK_NAME}:{up_down}{diff_prec}%\nHeadline: {article['title']}."
        f"\nBrief: {article['description']}" for article in first_three_articles
    ]

    client = Client(account_sid, auth_token)
    for article_msg in article:
        message = client.messages.create(
            body=article,
            from_="",
            to="",
        )
