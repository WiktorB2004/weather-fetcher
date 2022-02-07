## Weather Fetcher, GitHub: WiktorB2004, TODO Could add better error handling
import requests
import os
import math
from dotenv import load_dotenv
import urllib.parse

# environment variables setup
load_dotenv('./.env')
API_KEY = os.getenv('API_KEY')

city = input('\nPlease pass city name for forecast: ')
if type(city) == str:
    # Get coordinates of given city names
    location_data_res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={urllib.parse.quote_plus(city)}&limit=5&appid={API_KEY}')
    if location_data_res.status_code == 200:
        location_data = location_data_res.json()
        lat = location_data[0]['lat']
        lon = location_data[0]['lon']
        # Get weather data with given city coordinates
        weather_data_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric')
        # Print data to user
        if weather_data_response.status_code == 200:
            weather_data = weather_data_response.json()
            temperature = math.floor(weather_data['main']['temp'])
            description = (weather_data['weather'][0]['description']).capitalize()
            print(f'\nCity: {city.capitalize()}\nWeather: {description} \nTemperature: {temperature}\xb0')
        else:
            print(f'\n Something went wrong with fetching data about weather in {city.capitalize()}, status code: {location_data_res.status_code}')
    else: 
        print(f'\nSomething went wrong while fetching data about {city.capitalize()}, status code: {location_data_res.status_code}')
else:
    print('\nPlease pass city name')