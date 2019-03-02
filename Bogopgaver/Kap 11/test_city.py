import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """test city functions"""

    def test_city_country(self):
        test_of_city_country = city_country("santiago", "chile")
        self.assertEqual(test_of_city_country, "Santiago, Chile")

    def test_city_country_population(self):
        test_of_city_country = city_country("santiago", "chile", 1000)
        self.assertEqual(test_of_city_country, "Santiago, Chile - population 1000")

#unittest.main()