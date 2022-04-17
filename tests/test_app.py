from unittest.mock import patch, Mock
from unittest import TestCase
from models import CityWeatherData
from app import app

app.testing = True

class TestApp(TestCase):

    def setUp(self):
        self.city_object = CityWeatherData(
            city_name='Test City',
            country='TEST',
            min=10,
            max=20,
            feels_like=15
        )

    @patch('app.save_city_to_json', Mock())
    @patch('app.housekeep_cached_jsons', Mock())
    @patch('weather_api_requests.WeatherApiRequests.get_city_coordinates', Mock())
    @patch('weather_api_requests.WeatherApiRequests.get_city_temperature')
    def test_get_temperature(self, city_data_mock):
        city_data_mock.return_value = self.city_object
        with app.test_client() as client:
            response = client.get("/temperature/Teste")
        self.assertEqual(response.json, self.city_object.dict())
        self.assertEqual(response.status_code, 200)

    def test_get_temperature_404_error(self):
        with app.test_client() as client:
            response = client.get("/wrong_endpoint/Teste")
        self.assertEqual(response.status_code, 404)

    @patch('app.housekeep_cached_jsons', Mock())
    @patch('app.get_cached_jsons_from_tmp_folder')
    def test_get_last_temperatures(self, cached_cities):
        cached_cities.return_value = [
            'List of cities cached here'
        ]
        with app.test_client() as client:
            response = client.get("/temperature/max=10")
        self.assertEqual(response.json, {'latest_queried_cities': ['List of cities cached here']})
        self.assertEqual(response.status_code, 200)