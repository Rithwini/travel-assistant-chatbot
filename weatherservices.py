import requests
from utils.config import OPENWEATHER_API_KEY

class WeatherService:
    def get_weather(self, city):
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': OPENWEATHER_API_KEY, 'units': 'metric'}
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)
        print(response)
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather information for that location."
