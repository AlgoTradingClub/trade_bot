from trade_bot.models.Order import Order
from trade_bot.utils.Alpaca_Data import AlpacaData
from trade_bot.utils.CoinAPI_io import CoinAPI
from typing import List
from datetime import date
import sys


class Algorithm:
    def __init__(self):
        self.AlpacaData = AlpacaData()
        self.CoinAPI = CoinAPI()
        self.data = ""
        self.orders = []

    def before_trading(self) -> None:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError

    def trade(self, today: date) -> List[Order]:
        # TODO should i add a context variable to the parameters so the algo
        #  can know what current assets, cash, and positions I currently have?
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError

    def after_trading(self) -> None:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError

