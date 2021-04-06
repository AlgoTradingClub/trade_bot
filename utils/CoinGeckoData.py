from typing import Dict, List
import os
import pandas as pd
from datetime import datetime
# from models.settings import Settings
from utils.Min_Edit_Distance import levenshtein, min_edit_dist
from pycoingecko import CoinGeckoAPI


class CoinGecko:
    def __init__(self):
        """
        All free data and no API key necessary
        200 api calls/ min
        """
        self.api = CoinGeckoAPI()

    def get_price(self, symbols: List[str], currency="usd", print_error=True) -> float:
        resp = self.api.get_price(symbols, vs_currencies=currency)
        assert isinstance(symbols, list)
        if not resp:
            # got an empty response
            ...
            if print_error:
                print("No response. Please check the accuracy of your symbols and currencies.")
                print(self.__find_coin_id(symbols[0], self.get_all_coin_ids()))
            return None

        return resp

    def get_current_coin_price(self, symbols: List[str], currency='usd') -> str:
        """
        A wrapper function for 'python cli.py coin ...'
        :param symbols:
        :param currency:
        :return:
        """
        resp = self.api.get_price(symbols, vs_currencies=currency, print_error=False)
        assert isinstance(symbols, list)
        assert len(symbols) == 1
        s = ""
        if not resp:
            # bad coin name
            s += "No response. Please check the accuracy of your symbols.\n"
            s += self.__find_coin_id(symbols[0], self.get_all_coin_ids())
            return s

        elif not resp[symbols[0]]:
            # empty response
            s += "No response. Please check the accuracy of your currencies.\n"
            s += self.__find_currency_id(currency, self.get_supported_vs_currencies())
            return s
        else:
            s += f"Current price of {symbols[0]} vs {currency} is: {resp[symbols[0]][currency]}"
            return s

    def get_historical_data(self, symbol: str, days: int, currency='usd') -> pd.DataFrame:
        """
        By default, returns the the data in 1 hour time segments
        """
        assert isinstance(symbol, list)
        try:
            resp = self.api.get_coin_market_chart_by_id(symbol, currency, days)
        except ValueError as e:
            print(self.__find_coin_id(symbol[0], self.get_coins_list()))
            return None
        else:
            df = pd.DataFrame(columns=['price', 'marketCap', 'volume', 'time'])
            for i in range(len(resp['prices'])):
                timestamp = datetime.fromtimestamp(resp['prices'][i][0] / 1000)
                df = df.append({
                    'price': resp['prices'][i][1],
                    'marketCap': resp['market_caps'][i][1],
                    'volume': resp['total_volumes'][i][1],
                    'time': timestamp.isoformat()
                }, ignore_index=True)

            df = df.sort_values(by='time', ascending=False)
            df = df.reset_index(drop=True)
            return df

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

    def __find_currency_id(self, wrongCurr, allCurrs):
        suggestion = min_edit_dist(wrongCurr, allCurrs)
        return f"No data found for currency '{wrongCurr}'\n\n Did you mean '{suggestion}'?"


c = CoinGecko()