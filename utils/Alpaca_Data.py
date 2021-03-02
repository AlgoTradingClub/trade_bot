import alpaca_trade_api as tradeapi
import os
import pandas as pd
import datetime as date


class AlpacaData:
    def __init__(self, paper=True):
        """
        I don't think there's any different in the data quality between paper and live accounts.
        200 api calls/ min
        """
        base_url = "https://data.alpaca.markets/v2"
        if paper:
            key_id = "APCA_API_KEY_ID"
            secret_key = "APCA_API_SECRET_KEY"
        else:
            key_id = "APCA_API_KEY_ID_LIVE"
            secret_key = "APCA_API_SECRET_KEY_LIVE"

        key_id = os.environ[key_id]
        secret_key = os.environ[secret_key]

        self.api = tradeapi.REST(key_id, secret_key, base_url=base_url)
        self.api = tradeapi.REST()
        account = self.api.get_account()
        print(account.status)

    def get_bars_data(self, tickers: list, timeframe: str = 'day',
                      from_year: int = 2020, from_month: int = 1, from_day: int = 1,
                      to_year: int = 2021, to_month: int = 2, to_day: int = 26, limit=1000, ) -> pd.DataFrame:

        start = date.date(from_year, from_month, from_day).isoformat()
        end = date.date(to_year, to_month, to_day).isoformat()
        response = self.api.get_barset(tickers, timeframe, limit, start, end)

        data = {}
        for ticker in tickers:
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

        print("done")
        if len(data) == 1:
            k = data.keys()
            return data[tickers[0]]

        return data



