from models.Order import Order
from models.Data import Data
from utils.Alpaca_Data import AlpacaData
from utils.CoinAPI_io import CoinAPI
from utils.Polygon import Poly
from utils.CoinGeckoData import CoinGecko
from typing import List
from datetime import datetime
from models.Context import Context

NOT_IMPL_MSG = "I was not overridden in the child class. " \
               "\nExiting to prevent errors."


class Algorithm:
    def __init__(self):
        self.AlpacaData = AlpacaData()
        self.CoinAPI = CoinAPI()
        self.PolyApi = Poly()
        self.CoinGecko = CoinGecko()
        self.__data = dict()
        """
        A dictionary of historicalData (might expand later)
        EXAMPLE:
        {'AAPL': HistoricalData object AAPL,
        'TSLA': HistoricalData object TELSA}
        """
        self.__orders = []
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

    def add_order(self, o: Order) -> None:
        if isinstance(o, Order):
            self.__orders.append(o)

    def get_orders(self) -> List[Order]:
        return self.__orders

    def add_data(self, key: str, d: Data):
        if isinstance(d, Data):
            self.__data[key] = d

    def get_data(self, key: str):
        return self.__data[key]
