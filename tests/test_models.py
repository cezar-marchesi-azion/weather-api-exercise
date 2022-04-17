from unittest.mock import patch, Mock
from unittest import TestCase
from models import CityWeatherData, City



class TestModels(TestCase):

    
    def test_city_weather_data_init(self):
        result = CityWeatherData(
            city_name='Test City',
            country='TEST',
            min=30,
            max=40,
            feels_like=15
        )
        
        self.assertEqual(result.city_name, 'Test City')
        self.assertEqual(result.country, 'TEST')
        self.assertEqual(result.min, 30)
        self.assertEqual(result.max, 40)
        self.assertEqual(result.feels_like, 15)
        self.assertEqual(result.avg, 35)
    
    
    def test_city_init(self):
        result = City(
            city_name='Test City',
            country='TEST',
            lat=30,
            lon=40
        )
        
        self.assertEqual(result.city_name, 'Test City')
        self.assertEqual(result.country, 'TEST')
        self.assertEqual(result.lat, 30)
        self.assertEqual(result.lon, 40)