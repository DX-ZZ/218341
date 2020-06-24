import unittest
from city_functions import city_country
class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        city = 'santuago'
        country = 'chile'
        self.assertEqual(city_country(city, country), 'santuago chile')
unittest.main()