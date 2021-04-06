from models.Algo import Algorithm
from models.Order import Order
from models.Context import Context
from typing import List
from datetime import datetime
from utils.CoinGeckoData import CoinGecko

mypairs = "bitcoin", "eth"


class Pairs(Algorithm):
    def __init__(self):
        super(Pairs, self).__init__()

    def before_trading(self, first_trading_day: datetime, last_trading_day: datetime) -> None:
        cg = CoinGecko()
        btc = cg.get_historical_data(['bitcoin'], 30)
        eth = cg.get_historical_data(['ethereum'], 30)
        print("Got the data")

    def trade(self, today: datetime, context: Context) -> List[Order]:
        return self.orders

    def after_trading(self) -> None:
        ...


