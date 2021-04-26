from datetime import datetime
from pandas import DataFrame as DF

NOT_IMPL_MSG = "I was not overridden in the child class. " \
               "\nExiting to prevent errors."


class Data:
    def __init__(self, asset: str, price_data: DF, data_obj):
        if not isinstance(price_data, DF):
            raise ValueError("Price data must be a pandas dataframe")
        self.data = price_data
        self.__asset = asset
        self.__data_obj = data_obj

    def get_single_price(self, timestamp: datetime, flexible: bool) -> float:
        raise NotImplementedError(NOT_IMPL_MSG)

    def get_rolling_average(self, start_time: datetime, end_time: datetime, flexible: bool) -> float:
        raise NotImplementedError(NOT_IMPL_MSG)

    def get_current_price(self, today: datetime, flexible: bool):
        raise NotImplementedError(NOT_IMPL_MSG)

    def check_date_range(self, start_time: datetime, end_time: datetime, flexible: bool) -> float:
        raise NotImplementedError(NOT_IMPL_MSG)

    def try_load_data(self, source_obj, start_time: datetime, end_time: datetime) -> bool:
        """
        Tries to get data from data/
        :param source_obj:
        :param start_time:
        :param end_time:
        :return: True if able to load, False if not able to load from local data directory
        """
        raise NotImplementedError(NOT_IMPL_MSG)



    def set_data_obj(self, obj):
        self.__data_obj = obj