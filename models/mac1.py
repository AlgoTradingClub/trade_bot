from models.Algo import Algorithm
from models.Order import Order
from models.BarsData import BarsData
from models.Context import Context
from typing import List
from datetime import datetime, timedelta


class MAC(Algorithm):
    def __init__(self):
        super(MAC, self).__init__()

    def before_trading(self, first_trading_day: datetime, last_trading_day: datetime) -> None:
        if not isinstance(self.data, dict) or 'AAPL' not in self.data:
            hd = BarsData('AAPL')
            data = self.AlpacaData.get_bars_data("AAPL")  # TODO needs to change
            hd.load_df(data['AAPL'])
            self.data['AAPL'] = hd
        else:
            self.data["AAPL"].check_date_range(first_trading_day, last_trading_day)

    def trade(self, today: datetime, context: Context) -> List[Order]:
        assert isinstance(today, datetime)
        window = 7.0

        previous = today - timedelta(days=window)
        iso = previous.strftime("%Y-%m-%d")

        test = self.data["AAPL"].get_single_price(previous, flexible=True)
        rolling_test = self.data["AAPL"].get_rolling_average(previous, today)
        test2 = self.data["AAPL"].check_date_range(previous, today, flexible=True)
        curr = self.AlpacaData.get_bars_data("AAPL", timeframe='15Min', start=today, end=today, limit=5)
        # TODO get actual real market data. I htink i just ahve to get bars data at a smaller scale (hour or minute).
        curr_data = curr["AAPL"].at[curr["AAPL"].index[-1], 'close']  # getting most recent closing price

        if test < curr_data:
            # buy
            self.orders.append(Order("buy", "AAPL", 1))
        else:
            # sell
            self.orders.append(Order("sell", "AAPL", 1))
        return self.orders

    def after_trading(self) -> None:
        ...
