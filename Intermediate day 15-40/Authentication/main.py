import requests
import os
from twilio.rest import Client


# 6:00 UTC, run export env SID={account_sid};export env AUTH={auth_token}; python main.py
account_sid = os.environ.get('SID')
auth_token = os.environ.get('AUTH')

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 31.768318,
    "lon": 35.213711,
    "APPID": "",
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data['hourly'][:24]
will_rain = False
cloudy = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']

    if 500 <= condition_code < 600:
        will_rain = True

    if 800 <= condition_code <= 804:
        cloudy = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Will rain today.",
            from_="",
            to=""
        )
    print(message.status)

if cloudy:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Cloudy today.",
            from_="",
            to=""
        )
    print(message.status)
