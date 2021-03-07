from typing import Dict, List
import os
import pandas as pd
import datetime as date
from trade_bot.models.settings import Settings
from pycoingecko import CoinGeckoAPI


class CoinGecko:
    def __init__(self, paper=True):
        """
        I don't think there's any different in the data quality between paper and live accounts.
        200 api calls/ min
        """
        self.api = CoinGeckoAPI()

    def get_price(self, symbols: List[str], currency="usd"):
        resp = self.api.get_price(symbols, vs_currencies=currency)
        print(resp)
        return resp

    def get_historical_data(self, symbol: str, days: int, currency='usd'):
        """
        By default, returns the the data in 1 hour time segments
        """
        resp = self.api.get_coin_market_chart_by_id(symbol, currency, days)
        print(resp)
        return resp

    def get_supported_vs_currencies(self):
        """
        Returns the currencies that cryptos can be compared to . like 'usd'
        """
        return self.api.get_supported_vs_currencies()

    def get_coins_list(self):
        """
        Returns all the available crypto coins that are available
        """
        return self.api.get_coins_list()



