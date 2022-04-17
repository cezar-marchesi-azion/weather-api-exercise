import requests
from config import Configuration
from helpers import get_country_alpha_3
from models import City, CityWeatherData


class WeatherApiRequests:
    def __init__(self) -> None:
        self.api_key = Configuration.api_key
        self.weather_url = Configuration.weather_url
        self.get_city_coordinates_url = Configuration.get_city_coordinates_url

    def get_city_coordinates(self, city_name: str) -> City:
        url = self.url_builder(
            url=self.get_city_coordinates_url,
            city_name=city_name,
            api_key=self.api_key)

        r = requests.get(url).json()[0]

        country_alpha_3 = get_country_alpha_3(r['country'])

        return City(
            city_name=r['name'],
            lat=r['lat'],
            lon=r['lon'],
            country=country_alpha_3
        )


    def get_city_temperature(self, city: City) -> CityWeatherData:
        url = self.url_builder(
            url=self.weather_url,
            city_lat=str(city.lat),
            city_lon=str(city.lon),
            api_key=self.api_key
        )

        weather = requests.get(url).json()

        return CityWeatherData(
            city_name=city.city_name,
            country=city.country,
            min=weather['main']['temp_min'],
            max=weather['main']['temp_max'],
            feels_like=weather['main']['feels_like'],
        )
    
    @staticmethod
    def url_builder(**kwargs) -> str:
        url = kwargs.pop('url')    
        for k, v in kwargs.items():
            url = url.replace(k, v)
        return url