import alpaca_trade_api as tradeapi
from typing import Dict
import os
import pandas as pd
import datetime as date
from trade_bot.models.settings import Settings


class AlpacaData:
    def __init__(self, paper=True):
        """
        I don't think there's any different in the data quality between paper and live accounts.
        200 api calls/ min
        """
        key_names = Settings.keys_names
        base_url = "https://data.alpaca.markets"
        if paper:
            key_id = key_names["Alpaca Paper Key ID"]
            secret_key = key_names["Alpaca Paper Secret Key"]
        else:
            key_id = key_names["Alpaca Live Key ID"]
            secret_key = key_names["Alpaca Live Secret Key"]

        key_id = os.environ[key_id]
        secret_key = os.environ[secret_key]

        self.api = tradeapi.REST(key_id, secret_key, base_url=base_url)
        del key_id, secret_key

    def get_bars_data(self, tickers: list, timeframe: str = 'day',
                      from_year: int = 2020, from_month: int = 1, from_day: int = 1,
                      to_year: int = 2021, to_month: int = 2, to_day: int = 26, limit=1000, ) -> Dict[str, pd.DataFrame]:

        if isinstance(tickers, str):
            tickers = [tickers]

        assert isinstance(tickers, list)

        start = date.date(from_year, from_month, from_day).isoformat()
        end = date.date(to_year, to_month, to_day).isoformat()

        data = {}
        for ticker in tickers:
            response = self.api.get_barset(ticker, timeframe, limit, start, end)
            df = pd.DataFrame(columns=['close', 'open', 'high', 'low', 'volume', 'time'])
            for bar in response[ticker]:
                t = date.datetime.fromtimestamp(bar._raw['t'])
                df = df.append({'close': bar._raw['c'],
                                'open': bar._raw['o'],
                                'high': bar._raw['h'],
                                'low': bar._raw['l'],
                                'volume': bar._raw['v'],
                                'time': t.isoformat()},
                               ignore_index=True)
            data[ticker] = df

        return data

    def get_api(self):
        return self.api




