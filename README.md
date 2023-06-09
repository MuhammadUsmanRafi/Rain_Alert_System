# Rain_Alert_System
This code provides a rain alert system that sends SMS messages to a predefined phone number using the Twilio API. By using the OpenWeatherMap API, this code is able to retrieve weather data for a specific location and check if it will rain within the next 7 hours. If it detects that it will rain, the code sends an SMS message to a predefined phone number using the Twilio API.

#Prerequisites

An OpenWeatherMap API key

A Twilio account 


#Installation

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Update the API_KEY, OWN_ENDPOINT, account_sid, auth_token, lat, lon, from_ and to variables in the main.py file to the relevant values for your use case.

#Usage

Run the main.py file.
The code will check if it will rain within the next 7 hours and send an SMS message to the predefined phone number using the Twilio API if it detects that it will rain.

#Note: This code can be scheduled to run automatically using task scheduling tools like Cron for Linux or Task Scheduler for Windows.
