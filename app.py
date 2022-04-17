from flask import Flask
from flask_caching import Cache
from config import Configuration
from helpers import save_city_to_json, get_cached_jsons_from_tmp_folder, housekeep_cached_jsons
from weather_api_requests import WeatherApiRequests


DEFAULT_MAX_NUMBER = Configuration.default_max_number
CACHE_TTL = Configuration.cache_ttl

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'

cache = Cache()
cache.init_app(app)


@app.route("/temperature/<city_name>")
@cache.cached(timeout=CACHE_TTL)
def get_temperature(city_name):
    try:
        city = WeatherApiRequests().get_city_coordinates(
            city_name=city_name
        )

        city_info = WeatherApiRequests().get_city_temperature(
            city=city,
        )

        save_city_to_json(city_info.dict(), city.city_name)

        return city_info.dict()

    except Exception as ex:
        return "<h1>City not found</h1>"
    finally:
        housekeep_cached_jsons(CACHE_TTL)


@app.route("/temperature/max=", defaults={'max_number': DEFAULT_MAX_NUMBER})
@app.route("/temperature/max=<max_number>")
def get_last_temperatures(max_number):
    try:
        housekeep_cached_jsons(CACHE_TTL)
        city_list = {
            'latest_queried_cities': get_cached_jsons_from_tmp_folder(int(max_number))
        }
        return city_list
    except Exception as ex:
        return "<h1>Max must be integer</h1>"


@app.errorhandler(404)
def error(e):
    return "<h1>Oops, something went wrong</h1>", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7007)