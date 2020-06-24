import unittest
from name_function import format_name
from name_function import format_city


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formattedname = format_name('Tom', 'Hardy')
        self.assertEqual(formattedname, 'Tom Hardy')

    def test_first_middle_last_name(self):
        formattedname = format_name('Tom', 'Hardy')
        self.assertEqual(formattedname, 'Tom Hardy')

    def test_city_country(self):
        formattedcity = format_city('santiago', 'chile')
        self.assertEqual(formattedcity, 'Santiago,Chile')

    def test_city_country_population(self):
        formattedcity = format_city('santiago', 'chile', population='500000')
        self.assertEqual(formattedcity, 'Santiago,Chile - Population 500000')


if __name__ == 'main':
    unittest.main()
