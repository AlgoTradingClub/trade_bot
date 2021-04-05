from typing import Dict, List
import os
import pandas as pd
import datetime as date
# from models.settings import Settings
from utils.Min_Edit_Distance import levenshtein, min_edit_dist
import sys
print("PyTest Location: ", sys.executable)
from pycoingecko import CoinGeckoAPI


class CoinGecko:
    def __init__(self):
        """
        I don't think there's any different in the data quality between paper and live accounts.
        200 api calls/ min
        """
        self.api = CoinGeckoAPI()

    def get_price(self, symbols: List[str], currency="usd"):
        resp = self.api.get_price(symbols, vs_currencies=currency)
        assert isinstance(symbols, list)
        if not resp:
            # got an empty response
            ...
            print("No response. Please check the accuracy of your symbols and currencies.")
            print(self.__find_coin_id(symbols[0], self.get_all_coin_ids()))
            return None

        return resp

    def get_historical_data(self, symbol: str, days: int, currency='usd'):
        """
        By default, returns the the data in 1 hour time segments
        """
        assert isinstance(symbol, list)
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

    def get_all_coin_ids(self) -> set:
        """IDs are what must be used to get information from pycoingecko"""
        coins = self.get_coins_list()
        return set([coin['id'] for coin in coins])

    def __find_coin_id(self, wrongName, allIds):
        suggestion = min_edit_dist(wrongName, allIds)
        return f"No data found for symbol '{wrongName}'\n\n Did you mean '{suggestion}'?"


c = CoinGecko()