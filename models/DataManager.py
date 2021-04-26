from datetime import datetime
from models.BarsData import BarsData
from models.Data import Data


class DataSource:
    def __init__(self, source: str, source_obj, asset: str, first_day: datetime, last_day: datetime):
        self.__source = source
        self.__src_obj = source_obj
        self.__asset = asset
        self.__first_day = first_day
        self.__last_day = last_day


class DataManager:
    def __init__(self):
        self.__sources = {"ALPACA", "COINGECKO"}  # TODO add polygon and coin_api.io
        self.__timeframes = {"minute", "1Min", "5Min", "15Min", "day"}
        self.__data = dict()

    def set_data(self, source: str, asset: str, first_day: datetime, last_day: datetime, timeframe: str) -> None:
        if source.upper() not in self.__sources:
            raise ValueError(f"Given source {source} not available. "
                             f"\nPlease use one of the following:\n {self.__sources}")
        elif timeframe not in self.__timeframes:
            raise ValueError(f"Given timeframe {timeframe} not available \n "
                             f"Please enter one of the following:\n {self.__timeframes}")
        else:
            if source.upper() == "ALPACA":
                from utils.Alpaca_Data import AlpacaData
                asset = asset.upper()
                ad = AlpacaData()
                self.__data[asset] = {"data": BarsData(asset),
                                      'src_obj': ad}
                self.__data[asset].set_data_obj(ad)
                self.__data[asset].load_df(ad.get_bars_data(asset)[asset])
            else:
                ...

    def get_data(self, asset) -> Data:
        if asset not in self.__data:
            raise ValueError("Asset not found in data")
        else:
            return self.__data[asset]["Data"]

    def get_single_price(self, asset: str, date: datetime, flexible: bool = True) -> float:
        if asset not in self.__data:
            raise ValueError("Asset not found in data")
        else:
            return self.__data[asset].get_single_price(date, flexible)

    def get_rolling_average(self, asset: str, start_date: datetime, end_date: datetime, flexible: bool = True) -> float:
        if asset not in self.__data:
            raise ValueError("Asset not found in data")
        else:
            return self.__data[asset].get_rolling_average(start_date, end_date, flexible)

    def get_current_price(self, asset: str, now: datetime, flexible: bool = True):
        if asset not in self.__data:
            raise ValueError("Asset not found in data")
        else:
            return self.__data[asset].get_curent_price(now, flexible)

    def check_date_range(self, asset: str, start_date: datetime, end_date: datetime):
        """

        :param asset:
        :param start_date:
        :param end_date:
        :return:
        """
        pass


# TODO I should keep the data object only concerned with data and the datamanager able to get more data if necessary
#