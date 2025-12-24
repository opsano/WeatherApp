from django.shortcuts import render
from django.conf import settings
import requests
import os


# Create your views here.

# simple function based view which will only render the front end
def home(request):
    return render(request, 'home/home.html')

def weather(request):
    location = "San Diego" # this will be passed in through the front end later

    # commented out to use settings env variable of the api key 
    # key = os.getenv("WEATHER_API_KEY")
    key = settings.WEATHER_API_KEY
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"

    response = requests.get(url, timeout=10)
    response.raise_for_status() # will raise error if it occurred
    data = response.json()
    
    current = data["current"] # gets current weather data

    condition = current["condition"]["text"].lower()
    bg_class = "bg-sunny"

    if 'rain' in condition or 'drizzle' in condition or 'shower' in condition:
        bg_class = "bg-rainy"
    elif 'cloud' in condition or 'overcast' in condition:
        bg_class = "bg-cloudy"

    print(f"Weather Condition: '{condition}' -> Applied Class: '{bg_class}'") # Debugging line

    context = { # the data we care about
        "location": location, # added location
        "temp" : current["temp_f"],
        "clouds" : current["condition"]["text"],
        "humidity" : current["humidity"],
        "wind" : current["wind_mph"],
        "bg_class": bg_class,
    }

    return render(request, "home/weather.html", context)




