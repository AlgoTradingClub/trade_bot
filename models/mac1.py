from models.Algo import Algorithm
from models.Order import Order
from typing import List
from datetime import date

class mac(Algorithm):
    def __init__(self):
        super(mac, self).__init__()

    def before_trading(self) -> None:
        self.data = self.AlpacaData.get_bars_data("AAPL")
        print(self.data)

    def trade(self, today: date) -> List[Order]:
        return self.orders

    def after_trading(self) -> None:
        ...
