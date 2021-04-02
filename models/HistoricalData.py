from datetime import datetime
import pandas as pd
import logging
logger = logging.getLogger(__name__)


class HistoricalData:
    """
    A wrapper for the alpaca and polygon data to be used in the algorithms.
    This is stop rewriting code to access data in the algorithm
    Also to reduce the time to test code so that it doesn't have to retrieve every time in "before_testing"
    """
    def __init__(self):
        self.empty = True
        self.data = None

    def load_df(self, df: pd.DataFrame):
        # do stuff
        self.data = df
        # check the dataframe sort if necessary
        self.empty = False
        ...

    def check_empty(self) -> None:
        if self.empty:
            logger.error("No data found in HistoricalData Object. Aborting")
            raise LookupError

    def check_date_range(self, begin: datetime, end: datetime) -> bool:
        """
        The data can check to see if it has enough data to complete
        :return:
        """
        assert isinstance(begin, datetime) and isinstance(end, datetime)
        self.check_empty()

    def get_closing_price(self, d: datetime) -> float:
        """
        Return the closing price of the given day
        :param d:
        :return:
        """
        assert isinstance(d, datetime)
        self.check_empty()
        return 1.1

    def get_rolling_average(self, begin: datetime, end: datetime) -> float:
        assert isinstance(begin, datetime) and isinstance(end, datetime)
        self.check_empty()
        return 1.1