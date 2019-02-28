import unittest
from city_functions import city_country

class CityTest(unittest.TestCase):
    """Tests for city_functions"""

    def test_city_country(self):
        """does input like 'santiago, chile' work"""
        formatted_city_country = city_country("santiago", "chile")
        self.assertEqual(formatted_city_country, "Santiago, Chile")