from models.Order import Order
from utils.Alpaca_Data import AlpacaData
from utils.CoinAPI_io import CoinAPI
from utils.Polygon import Poly
from utils.CoinGeckoData import CoinGecko
from typing import List
from datetime import datetime
from models.Context import Context
import sys

NOT_IMPL_MSG = "I was not overridden in the child class. Exiting to prevent errors."


class Algorithm:
    def __init__(self):
        self.AlpacaData = AlpacaData()
        self.CoinAPI = CoinAPI()
        self.PolyApi = Poly()
        self.CoinGecko = CoinGecko()
        self.data = dict()
        """
        A dictionary of historicalData (might expand later)
        EXAMPLE:
        {'AAPL': HistoricalData object AAPL,
        'TSLA': HistoricalData object TELSA}
        """
        self.orders = []
        """
        A list of Order objects
        """

    def before_trading(self, first_trading_day: datetime, last_trading_day: datetime) -> None:
        raise NotImplementedError(NOT_IMPL_MSG)

    def trade(self, today: datetime, context: Context) -> List[Order]:
        print("I was not overridden in the child class. Exiting to prevent errors.")
        raise NotImplementedError(NOT_IMPL_MSG)

    def after_trading(self) -> None:
        raise NotImplementedError(NOT_IMPL_MSG)

