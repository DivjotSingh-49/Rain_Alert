import requests
import os
from twilio.rest import Client

api_key=os.environ.get("OWM_API_KEY")
OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
twilio_sid=os.environ.get("TWILIO_SID")
twilio_token=os.environ.get("TWILIO_AUTH_TOKEN")

lat=31.633980
long=74.872261
weather_prams={"lat":lat,"lon":long,"appid":api_key,"cnt":4}

response=requests.get(OWM_Endpoint,params=weather_prams)
response.raise_for_status()
weather_data=response.json()

will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code<700:
        will_rain=True
if will_rain:
   client = Client(twilio_sid,twilio_token)
   message = client.messages.create(
    body="It's going to rain today, Remember to bring an Umbrella!.",
    from_="+13503535873",
    to="+918699828879",
)
   print(message.status)
