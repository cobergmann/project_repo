import datetime
import unittest
from project_repo import weather_api

class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = weather_api.search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)

    def test_search_city_for_london(self):
        city = weather_api.search_city('London')
        self.assertEqual(city['title'], 'London')
        self.assertEqual(city['woeid'], 44418)

    def test_search_city_for_unknown_city(self):
        city = weather_api.search_city('Rouen')
        self.assertEqual(city, None)

    def test_search_city_ambiguous_city(self):
        weather_api.input = lambda _: "1"
        city = weather_api.search_city('San')
        self.assertEqual(city['title'], 'San Francisco')

    def test_weather_forecast(self):
        forecast = weather_api.weather_forecast(44418)
        self.assertIsInstance(
            forecast, list, "Did you select the `consolidated_weather` key?")
        self.assertEqual(forecast[0]['applicable_date'],
                         datetime.date.today().strftime('%Y-%m-%d'))
