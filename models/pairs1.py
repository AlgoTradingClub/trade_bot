from models.Algo import Algorithm
from models.Order import Order
from models.Context import Context
from typing import List
from datetime import datetime


class Pairs(Algorithm):
    def __init__(self):
        super(Pairs, self).__init__()

    def before_trading(self, first_trading_day: datetime, last_trading_day: datetime) -> None:
        ...

    def trade(self, today: datetime, context: Context) -> List[Order]:
        return self.orders

    def after_trading(self) -> None:
        ...


