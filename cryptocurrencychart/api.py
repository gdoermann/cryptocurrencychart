from cryptocurrencychart.config import parser
from cryptocurrencychart import urls
from functools import lru_cache
import datetime
import requests
import requests.auth


class CryptoCurrencyChartApi:
    BASE = parser.get('default', 'BASE_CURRENCY', fallback='USD')

    def __init__(self, api_key: str = None, api_secret: str = None):
        self.key = api_key or parser.get('default', 'KEY')
        self.secret = api_secret or parser.get('default', 'SECRET')
        self.session = requests.session()
        self.session.auth = requests.auth.HTTPBasicAuth(self.key, self.secret)
        self._coin_dict = None

    def _url(self, part, **kwargs):
        fkwargs = {k: self._format(v) for k, v in kwargs.items()}
        return urls.BASE + part.format(**fkwargs)

    def _format(self, value):
        if isinstance(value, (datetime.date, datetime.datetime)):
            value = value.strftime('%Y-%m-%d')
        return value

    @lru_cache()
    def get_base_currencies(self):
        url = self._url(urls.GET_BASE_CURRENCIES)
        return self.get(url)['baseCurrencies']

    @lru_cache()
    def get_coins(self):
        url = self._url(urls.GET_COINS)
        return self.get(url)['coins']

    @lru_cache()
    def get_data_types(self):
        url = self._url(urls.GET_DATA_TYPES)
        return self.get(url)

    def set_base_currency(self, currency, validate=True):
        if validate:
            currencies = self.get_base_currencies()
            if currency not in currencies:
                raise ValueError('Invalid base currency: {}'.format(currency))
        self.BASE = currency

    def view_coin(self, coin: int, date: datetime.date, base_currency: str = None):
        if base_currency is None:
            base_currency = self.BASE
        url = self._url(urls.VIEW_COIN, coin=coin, date=date, base=base_currency)
        return self.get(url)['coin']

    def view_coin_history(self, coin: int, start: datetime.date, 
            end: datetime.date, dtype: str ='marketCap', base_currency: str = None):
        if base_currency is None:
            base_currency = self.BASE
        url = self._url(urls.VIEW_COIN_HISTORY, coin=coin, start=start, 
                dtype=dtype,
                end=end, base=base_currency)
        return self.get(url)

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        response.raise_for_status()
        return response.json()

    @property
    def coin_dict(self):
        if not self._coin_dict:
            coins = self.get_coins()
            self._coin_dict = {i['code']: i for i in coins}
        return self._coin_dict

    def __getitem__(self, item):
        return self.coin_dict[item]

    def __contains__(self, item):
        return item in self.coin_dict

    def close(self):
        self.session.close()

    def __del__(self):
        self.close()
