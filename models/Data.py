from datetime import datetime
from pandas import DataFrame as DF

NOT_IMPL_MSG = "I was not overridden in the child class. " \
               "\nExiting to prevent errors."


class Data:
    def __init__(self, asset: str, price_data: DF):
        self.data = price_data
        self.__asset = asset
        self.__data_obj = None

    def get_single_price(self, timestamp: datetime, flexible: bool) -> float:
        raise NotImplementedError(NOT_IMPL_MSG)

    def get_rolling_average(self, start_time: datetime, end_time: datetime, flexible: bool) -> float:
        raise NotImplementedError(NOT_IMPL_MSG)

    def get_current_price(self, today: datetime, flexible: bool):
        raise NotImplementedError(NOT_IMPL_MSG)

    def check_date_range(self, start_time: datetime, end_time: datetime, flexible: bool) -> float:
        raise NotImplementedError(NOT_IMPL_MSG)

    def set_data_obj(self, obj):
        self.__data_obj = obj

    def fetch_or_load_data(self, source_obj, start_time: datetime, end_time: datetime) -> None:
        raise NotImplementedError(NOT_IMPL_MSG)