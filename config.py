import os
from dotenv import load_dotenv

load_dotenv()


class Configuration:
    api_key = os.environ.get('WEATHER_APPID', '')
    cache_ttl = int(os.environ.get('CACHE_TTL', 300))
    default_max_number = int(os.environ.get('DEFAULT_MAX_NUMBER', 5))
    get_city_coordinates_url = "http://api.openweathermap.org/geo/1.0/direct?q=city_name&appid=api_key"
    weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=city_lat&lon=city_lon&units=metric&appid=api_key"
