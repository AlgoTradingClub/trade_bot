from Order import Order
from ..utils.Alpaca_Data import AlpacaData
from ..utils.CoinAPI_io import CoinAPI
import sys


class Algorithm:
    def __init__(self):
        self.AlpacaData = AlpacaData()
        self.CoinAPI = CoinAPI()

    def before_trading(self) -> None:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        sys.exit(1)

    def trade(self) -> Order:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        sys.exit(1)

    def after_trading(self) -> None:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        sys.exit(1)

