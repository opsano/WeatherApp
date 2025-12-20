from django.shortcuts import render
import requests
import os


# Create your views here.

# simple function based view which will only render the front end
def home(request):
    return render(request, 'home/home.html')

def weather(request):
    location = "San Diego" # this will be passed in through the front end later
    key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"

    response = requests.get(url, timeout=10)
    response.raise_for_status() # will raise error if it occurred
    data = response.json()
    
    current = data["current"] # gets current weather data

    context = { # the data we care about
        "temp" : current["temp_f"],
        "clouds" : current["condition"]["text"],
        "humidity" : current["humidity"],
        "wind" : current["wind_mph"],
    }

    return render(request, "weather.html", context)
    



