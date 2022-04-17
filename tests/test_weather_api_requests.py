from unittest.mock import patch, Mock
from unittest import TestCase
from weather_api_requests import WeatherApiRequests
from models import City, CityWeatherData


class TestWeatherApiRequests(TestCase):

    def setUp(self):
        self.weather_api_requests = WeatherApiRequests()
        self.city = City(
            city_name='Test City',
            country='TEST',
            lat=10,
            lon=20
        )

    @patch('weather_api_requests.WeatherApiRequests.url_builder', Mock())
    @patch('weather_api_requests.get_country_alpha_3')
    @patch('weather_api_requests.requests.get')
    def test_get_city_coordinates(self, mock_response, mock_country_code):
        mock_response.return_value = MockCityResponse()
        mock_country_code.return_value = "TES"
        result = self.weather_api_requests.get_city_coordinates('Teste')
        self.assertIsInstance(result, City)

    @patch('weather_api_requests.WeatherApiRequests.url_builder', Mock())
    @patch('weather_api_requests.requests.get')
    def test_get_city_temperature(self, mock_response):
        mock_response.return_value = MockTemperatureResponse()
        result = self.weather_api_requests.get_city_temperature(self.city)
        self.assertIsInstance(result, CityWeatherData)

    def test_url_builder(self):
        url = "https://test.com/test_this"
        test_this = "result_here"
        result = self.weather_api_requests.url_builder(
            url=url,
            test_this=test_this
        )
        self.assertEqual(result,
                         "https://test.com/result_here")


class MockCityResponse:
    def json(self):
        return [
            {
                "name": "Test City",
                "country": "Test Country",
                "lat": 10,
                "lon": 20
            }
        ]


class MockTemperatureResponse:
    def json(self):
        return {
            "main": {
                'temp_min': 10,
                'temp_max': 20,
                'feels_like': 30
            }
        }
