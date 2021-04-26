from models.Algo import Algorithm
from models.Order import Order
from models.BarsData import BarsData
from models.Context import Context
from models.DataManager import DataManager
from typing import List
from datetime import datetime, timedelta


class MAC(Algorithm):
    def __init__(self):
        super(MAC, self).__init__()
        self.dm = DataManager()

    def before_trading(self, first_trading_day: datetime, last_trading_day: datetime) -> None:
        self.dm.set_data('ALPACA', "AAPL", first_trading_day, last_trading_day, 'day')
        # if not isinstance(self.data, dict) or 'AAPL' not in self.data:
        #     hd = BarsData('AAPL')
        #     data = self.AlpacaData.get_bars_data("AAPL")  # TODO needs to change
        #     hd.load_df(data['AAPL'])
        #     self.data['AAPL'] = hd
        # else:
        #     self.data["AAPL"].check_date_range(first_trading_day, last_trading_day)

    def trade(self, today: datetime, context: Context) -> List[Order]:
        assert isinstance(today, datetime)
        window = 7.0

        previous = today - timedelta(days=window)
        iso = previous.strftime("%Y-%m-%d")

        test = self.dm.get_single_price("AAPL", previous, flexible=True)
        rolling_test = self.dm.get_single_price.get_rolling_average("AAPL", previous, today)
        test2 = self.dm.check_date_range("AAPL", previous, today, flexible=True)
        curr = self.AlpacaData.get_bars_data("AAPL", timeframe='15Min', start=today, end=today, limit=5)
        curr_data = curr["AAPL"].at[curr["AAPL"].index[-1], 'close']  # getting most recent closing price

        if test < curr_data:
            # buy
            self.add_order((Order("buy", "AAPL", 1)))
        else:
            # sell
            self.add_order((Order("sell", "AAPL", 1)))
        return self.orders

    def after_trading(self) -> None:
        ...
