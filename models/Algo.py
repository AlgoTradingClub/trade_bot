from models.Order import Order
from utils.Alpaca_Data import AlpacaData
from utils.CoinAPI_io import CoinAPI
from utils.Polygon import Poly
from typing import List
from datetime import date
import sys

NOT_IMPL_MSG = "I was not overridden in the child class. Exiting to prevent errors."

class Algorithm:
    def __init__(self):
        self.AlpacaData = AlpacaData()
        self.CoinAPI = CoinAPI()
        self.PolyApi = Poly()
        self.data = ""
        self.orders = []

    def before_trading(self) -> None:
        raise NotImplementedError(NOT_IMPL_MSG)

    def trade(self, today: date) -> List[Order]:
        # TODO should i add a context variable to the parameters so the algo
        #  can know what current assets, cash, and positions I currently have?
        raise NotImplementedError(NOT_IMPL_MSG)

    def after_trading(self) -> None:
        raise NotImplementedError(NOT_IMPL_MSG)

