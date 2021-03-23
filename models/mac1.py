from models.Algo import Algorithm
from models.Order import Order
from typing import List
from datetime import date, datetime, timedelta


class MAC(Algorithm):
    def __init__(self):
        super(MAC, self).__init__()

    def before_trading(self) -> None:
        self.data = self.AlpacaData.get_bars_data("AAPL")  # TODO needs to change

    def trade(self, today: date) -> List[Order]:
        assert isinstance(today, datetime)
        window = 7.0

        previous = today - timedelta(days=window)
        iso = previous.strftime("%Y-%m-%d")
        df = self.data["AAPL"]
        p_data = df.loc[df['time'] == iso]['close'].values[0]  # getting close price in the past

        curr = self.AlpacaData.get_bars_data("AAPL", 'day', today.year, today.month, today.day,
                                      today.year, today.month, today.day, limit=5)
        curr_data = curr["AAPL"].at[curr["AAPL"].index[-1], 'close']  # getting most recent closing price

        if p_data < curr_data:
            # buy
            self.orders.append(Order("buy", "AAPL", 1))
        else:
            # sell
            self.orders.append(Order("sell", "AAPL", 1))
        return self.orders

    def after_trading(self) -> None:
        ...
