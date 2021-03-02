from trade_bot.models.Algo import Algorithm
from trade_bot.models.Order import Order
from typing import List
from datetime import date


class Pairs(Algorithm):
    def __init__(self):
        super(Pairs, self).__init__()

    def before_trading(self) -> None:
        ...

    def trade(self, today: date) -> List[Order]:
        return self.orders

    def after_trading(self) -> None:
        ...


