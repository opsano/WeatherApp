from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import requests
import os


# Create your views here.

# simple function based view which will only render the front end
def home(request):
    return render(request, 'home/home.html')

def search_page(request):
    return render(request, "home/search.html")

#this function will be used to get autocomplete suggestions for city names
def searchAutoComplete(request):
    query = request.GET.get('q','').strip()
    if not query:
        return JsonResponse([], safe=False)
    
    key = settings.WEATHER_API_KEY
    url = f"http://api.weatherapi.com/v1/search.json?key={key}&q={query}"
    response = requests.get(url, timeout=10)
    data=response.json()

    names = []
    urls = []
    for item in data:
        names.append(f"{item['name']}, {item['region']}, {item['country']}")
        urls.append(item['url'])
    responseData = {'names': names, 'urls': urls}
    pprint(responseData)
    return JsonResponse(responseData, safe=False)


def weather(request):
    location = request.GET.get('q') # this will be passed in through the front end later

    # commented out to use settings env variable of the api key 
    # key = os.getenv("WEATHER_API_KEY")
    key = settings.WEATHER_API_KEY
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"

    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        location = "San Diego"
        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"
        response = requests.get(url, timeout=10)
    data = response.json()
    current = data["current"] # gets current weather data
    location = data["location"]

    condition = current["condition"]["text"].lower()
    bg_class = "bg-sunny"

    if 'rain' in condition or 'drizzle' in condition or 'shower' in condition:
        bg_class = "bg-rainy"
    elif 'cloud' in condition or 'overcast' in condition:
        bg_class = "bg-cloudy"

    print(f"Weather Condition: '{condition}' -> Applied Class: '{bg_class}'") # Debugging line

    context = { # the data we care about
        "local_time" : location["localtime"],
        "location": location["name"], # added location
        "temp" : current["temp_f"],
        "condition" : current["condition"]["text"],
        "humidity" : current["humidity"],
        "wind" : current["wind_mph"],
        "bg_class": bg_class,
    }

    return render(request, "home/weather.html", context)




