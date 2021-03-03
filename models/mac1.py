from trade_bot.models.Algo import Algorithm
from trade_bot.models.Order import Order
from typing import List
from datetime import date


class MAC(Algorithm):
    def __init__(self):
        super(MAC, self).__init__()

    def before_trading(self) -> None:
        self.data = self.AlpacaData.get_bars_data("AAPL") # TODO needs to change

    def trade(self, today: date) -> List[Order]:
        return self.orders

    def after_trading(self) -> None:
        ...
