import requests
from config import API_KEY, BASE_URL


class WeatherClient:
    def __init__(self):
        self.api_key= API_KEY
        self.base_url = BASE_URL
        
    def get_weather_by_city(self, city:str):
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()