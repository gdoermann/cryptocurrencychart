import unittest
from cryptocurrencychart.api import CryptoCurrencyChartApi


class TestApi(unittest.TestCase):
    def test_api_connection(self):
        api = CryptoCurrencyChartApi()
        currencies = api.get_base_currencies()
        self.assertTrue('baseCurrencies' in currencies)
        self.assertTrue('USD' in currencies['baseCurrencies'])

    def test_set_base_currency(self):
        api = CryptoCurrencyChartApi()
        api.set_base_currency('USD', validate=False)
        self.assertEqual(api.BASE, 'USD')
        api.set_base_currency('CZK', validate=True)
        self.assertEqual(api.BASE, 'CZK')
        self.assertRaises(ValueError, api.set_base_currency, 'GBALK', validate=True)
        self.assertEqual(api.BASE, 'CZK')
        api.set_base_currency('GBALK', validate=False)
        self.assertEqual(api.BASE, 'GBALK')
        api.set_base_currency('USD', validate=False)
        self.assertEqual(api.BASE, 'USD')
