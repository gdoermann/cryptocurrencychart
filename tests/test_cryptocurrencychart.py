import datetime
import unittest
from cryptocurrencychart.api import CryptoCurrencyChartApi


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.reset()

    def reset(self):
        self.api = CryptoCurrencyChartApi()

    def test_api_connection(self):
        currencies = self.api.get_base_currencies()
        self.assertTrue('USD' in currencies)

    def test_set_base_currency(self):
        self.api.set_base_currency('USD', validate=False)
        self.assertEqual(self.api.BASE, 'USD')
        self.api.set_base_currency('CZK', validate=True)
        self.assertEqual(self.api.BASE, 'CZK')
        self.assertRaises(ValueError, self.api.set_base_currency, 'GBALK', validate=True)
        self.assertEqual(self.api.BASE, 'CZK')
        self.api.set_base_currency('GBALK', validate=False)
        self.assertEqual(self.api.BASE, 'GBALK')
        self.api.set_base_currency('USD', validate=False)
        self.assertEqual(self.api.BASE, 'USD')
        self.reset()

    def test_get_coins(self):
        coins = self.api.get_coins()
        self.assertIsNotNone(coins)
        self.assertIsInstance(coins, list)

    def test_view_coin(self):
        btc = self.api.coin_dict.get('BTC')
        response = self.api.view_coin(btc['id'], datetime.date.today() - datetime.timedelta(days=1), 'USD')
        self.assertEqual(response['baseCurrency'], 'USD')

    def test_view_coin_history(self):
        btc = self.api.coin_dict.get('BTC')
        end = datetime.date.today() - datetime.timedelta(days=1)
        start = end - datetime.timedelta(days=30)
        response = self.api.view_coin_history(btc['id'], start, end, 'USD')
        self.assertEqual(response['baseCurrency'], 'USD')
