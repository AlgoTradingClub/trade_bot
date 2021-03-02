import os
import pandas as pd
from trade_bot.utils.restapi_coinapi_io import CoinAPIv1
import datetime
from trade_bot.models.settings import Settings


period_ids = {
    '1SEC', '2SEC', '3SEC', '4SEC', '5SEC', '6SEC', '10SEC', "15SEC", "20SEC", "30SEC",
    '1MIN', '2MIN', '3MIN', '4MIN', '5MIN', '6MIN', '10MIN', '15MIN', '20MIN', '30MIN',
    '1HRS', '2HRS', '3HRS', '4HRS', '6HRS', '8HRS', '12HRS',
    '1DAY', '2DAY', '3DAY', '5DAY', '7DAY', '10DAY',
    '1MTH', '2MTH', '3MTH', '4MTH', "6MTH",
    '1YRS', '2YRS', '3YRS', '4YRS', "5YRS",
}


class CoinAPI:
    """
    This API has access to 11003 crypto coins and more come out all the time. HODL BTC!
    Something to be aware of if how crypto works. Since its sort of a currency, you have to compare it to a known
    currency. For example, when you ask the price of bitcoin, you also need to tell the api what currency to compare it
    to, i.e. USD.

    So for the functions:
        get_current_exchange_rate
        get_date_exchange_rate
        bars_latest_data
        get_daily_data
    The FIRST symbol, sym1, is the crypto, and the SECOND symbol, sym2, is the comparative currency.
    """
    def __init__(self):
        try:
            coinapi_key = Settings.keys_names["Coinbase Key"]
            self.api_key = os.environ[coinapi_key]
            del coinapi_key
        except KeyError as k:
            print(k.__str__())
            print("API Key for the CoinAPI.io not found.\n"
                  "Please get an API key from https://www.coinapi.io/ "
                  "and place the key in your system environment variables\n"
                  "Save the variable with the name of 'coinapi_io_key'")
        else:
            self.api = CoinAPIv1(self.api_key)

    def get_daily_data(self, ticker1: str = "BTC", ticker2: str = "USD", time_interval: str = "1DAY",
                       start_year: int = 2020, start_month: int = 1, start_day: int = 1,
                       end_year: int = 2021, end_month: int = 1, end_day: int = 1) -> pd.DataFrame:

        start = datetime.date(start_year, start_month, start_day).isoformat()
        end = datetime.date(end_year, end_month, end_day).isoformat()
        ohlcv_historical = self.api.ohlcv_historical_data(f'BITSTAMP_SPOT_{ticker1}_{ticker2}',
                                                     {'period_id': time_interval,
                                                      'time_start': start,
                                                      'time_end': end})

        df = pd.DataFrame(columns=['open', 'close', 'high', 'low', 'volume', 'trades', 'period_start'])

        for period in ohlcv_historical:
            d = {
                'open': period['price_open'],
                'close': period['price_close'],
                'high': period['price_high'],
                'low': period['price_low'],
                'volume': period['volume_traded'],
                'trades': period['trades_count'],
                'period_start': period['time_period_start']
            }
            df = df.append(d, ignore_index=True)
            print('Period start: %s' % period['time_period_start'])
            print('Period end: %s' % period['time_period_end'])
            print('Time open: %s' % period['time_open'])
            print('Time close: %s' % period['time_close'])
            print('Price open: %s' % period['price_open'])
            print('Price close: %s' % period['price_close'])
            print('Price low: %s' % period['price_low'])
            print('Price high: %s' % period['price_high'])
            print('Volume traded: %s' % period['volume_traded'])
            print('Trades count: %s' % period['trades_count'])
        return df

    def print_exchanges(self):
        exchanges = self.api.metadata_list_exchanges()

        print('Exchanges')
        for exchange in exchanges:
            print('Exchange ID: %s' % exchange['exchange_id'])
            print('Exchange website: %s' % exchange['website'])
            print('Exchange name: %s' % exchange['name'])
            print("...")

    def print_asset(self):
        assets = self.api.metadata_list_assets()
        print('Assets')
        for asset in assets:
            print('Asset ID: %s' % asset['asset_id'])
            try:
                print('Asset name: %s' % asset['name'])
            except KeyError:
                print('Can not find name')
            print('Asset type (crypto?): %s' % asset['type_is_crypto'])

    def print_symbols(self):
        symbols = self.api.metadata_list_symbols()
        print('Symbols')
        for symbol in symbols:
            print('Symbol ID: %s' % symbol['symbol_id'])
            print('Exchange ID: %s' % symbol['exchange_id'])
            print('Symbol type: %s' % symbol['symbol_type'])
            try:
                print('Asset ID base: %s' % symbol['asset_id_base'])
            except KeyError:
                print('Can not find Asset ID base')
            try:
                print('Asset ID quote: %s' % symbol['asset_id_quote'])
            except KeyError:
                print('Can not find Asset ID quote')

            if (symbol['symbol_type'] == 'FUTURES'):
                print('Future delivery time: %s' % symbol['future_delivery_time'])

            if (symbol['symbol_type'] == 'OPTION'):
                print('Option type is call: %s' % symbol['option_type_is_call'])
                print('Option strike price: %s' % symbol['option_strike_price'])
                print('Option contract unit: %s' % symbol['option_contract_unit'])
                print('Option exercise style: %s' % symbol['option_exercise_style'])
                print('Option expiration time: %s' % symbol['option_expiration_time'])

    def get_current_exchange_rate(self, sym1: str = "BTC", sym2: str = "USD"):
        exchange_rate = self.api.exchange_rates_get_specific_rate(sym1, sym2)
        print('Time: %s' % exchange_rate['time'])
        print('Base: %s' % exchange_rate['asset_id_base'])
        print('Quote: %s' % exchange_rate['asset_id_quote'])
        print('Rate: %s' % exchange_rate['rate'])

    def get_date_exchange_rate(self, sym1: str = "BTC", sym2: str = "USD",
                               year: int = 2021, month: int = 1, day: int = 1):
        date = datetime.date(year, month, day).isoformat()
        exchange_rate_last_week = self.api.exchange_rates_get_specific_rate(sym1, sym2, {'time': date})
        print('Time: %s' % exchange_rate_last_week['time'])
        print('Base: %s' % exchange_rate_last_week['asset_id_base'])
        print('Quote: %s' % exchange_rate_last_week['asset_id_quote'])
        print('Rate: %s' % exchange_rate_last_week['rate'])

    def get_all_current_rates(self, sym: str = "BTC"):
        current_rates = self.api.exchange_rates_get_all_current_rates(sym)

        print("Asset ID Base: %s" % current_rates['asset_id_base'])
        for rate in current_rates['rates']:
            print('Time: %s' % rate['time'])
            print('Quote: %s' % rate['asset_id_quote'])
            print('Rate: %s' % rate['rate'])

    def bars_list_all_periods(self):
        periods = self.api.ohlcv_list_all_periods()

        for period in periods:
            print('ID: %s' % period['period_id'])
            print('Seconds: %s' % period['length_seconds'])
            print('Months: %s' % period['length_months'])
            print('Unit count: %s' % period['unit_count'])
            print('Unit name: %s' % period['unit_name'])
            print('Display name: %s' % period['display_name'])

    def bars_latest_data(self, sym1: str = "BTC", sym2: str = "USD", timespan: str = "1MIN"):
        if timespan not in period_ids:
            return f"The timespan you gave of {timespan} is not in the possible time units."

        ohlcv_latest = self.api.ohlcv_latest_data(f"BITSTAMP_SPOT_{sym1}_{sym2}", {'period_id': timespan})

        for period in ohlcv_latest:
            print('Period start: %s' % period['time_period_start'])
            print('Period end: %s' % period['time_period_end'])
            print('Time open: %s' % period['time_open'])
            print('Time close: %s' % period['time_close'])
            print('Price open: %s' % period['price_open'])
            print('Price close: %s' % period['price_close'])
            print('Price low: %s' % period['price_low'])
            print('Price high: %s' % period['price_high'])
            print('Volume traded: %s' % period['volume_traded'])
            print('Trades count: %s' % period['trades_count'])
