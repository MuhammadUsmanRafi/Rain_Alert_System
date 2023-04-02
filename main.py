import requests
from twilio.rest import Client
import time
import schedule

API_KEY = "YOUR_API_KEY"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

parameter = {
    "lat": "Floating_YOUR_LATITUDE",
    "lon": "Floating_YOUR_LONGITUDE",
    "appid": API_KEY
}

def send_message():
    response = requests.get(url=OWN_ENDPOINT, params=parameter)
    response.raise_for_status()
    data = response.json()

    if int(data["weather"][0]["id"]) > 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an umbrella☂️.",
            from_="YOUR_TWILIO_PHONE_NUMBER",
            to="YOUR_PHONE_NUMBER"
        )
        print(message.status)

schedule.every(24).hours.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
