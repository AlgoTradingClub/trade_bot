from models.Order import Order
from utils.Alpaca_Data import AlpacaData
from utils.CoinAPI_io import CoinAPI
from utils.Polygon import Poly
from typing import List
from datetime import datetime
from models.Context import Context
import sys


class Algorithm:
    def __init__(self):
        self.AlpacaData = AlpacaData()
        self.CoinAPI = CoinAPI()
        self.PolyApi = Poly()
        self.data = ""
        self.orders = []

    def before_trading(self) -> None:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError

    def trade(self, today: datetime, context: Context) -> List[Order]:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError

    def after_trading(self) -> None:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError

