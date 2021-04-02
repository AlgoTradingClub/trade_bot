from datetime import datetime, timedelta
import pandas as pd
import re
import logging
logger = logging.getLogger(__name__)


class HistoricalData:
    """
    A wrapper for the alpaca and polygon data to be used in the algorithms.
    This is stop rewriting code to access data in the algorithm
    Also to reduce the time to test code so that it doesn't have to retrieve every time in "before_testing"
    """
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.empty = True
        self.data = None
        self.granular_data = False

    def load_df(self, df: pd.DataFrame):
        # do stuff
        assert isinstance(df, pd.DataFrame)
        required_cols = {'low', 'high', 'open', 'close', 'time'}
        assert all(any(req in col for col in set(df.columns)) for req in required_cols)
        df = self.validate_df(df)
        if not df.empty:
            self.data = df
            self.empty = False
        else:
            logger.error(f"The dataframe was rejected by 'validate_df'.\n {str(df)}")
            raise ValueError("The dataframe was rejected by 'validate_df' ")

    def validate_df(self, df) -> pd.DataFrame:
        df = df.sort_values(by='time', ascending=False)
        df = df.reset_index(drop=True)
        time_value = df['time'].values
        # check the format of the time col
        if all(bool(re.search(r"\d{4}-\d{2}-\d{2}\b", v)) for v in time_value):
            return df
        elif all(bool(re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{0,6}\b", v)) for v in time_value):
            self.granular_data = True
            # This historical data has more than one piece of data per day
            return df
        else:
            return pd.DataFrame()

    def check_empty(self) -> None:
        if self.empty or not isinstance(self.data, pd.DataFrame) or self.data.empty:
            logger.error("No data found in HistoricalData Object. Aborting")
            raise LookupError

    def check_date_range(self, begin: datetime, end: datetime) -> bool:
        """
        The data can check to see if it has enough data to complete
        :return:
        """
        assert isinstance(begin, datetime) and isinstance(end, datetime)
        self.check_empty()

    def get_single_price(self, d: datetime, flexible=False, category: str = "close") -> float:
        """
        Return the closing/opening/etc price for a given day
        :param d: the date of the price
        :param flexible: If the user asks for a closing price that doesn't exist (weekend or holiday), it will return
        data from the next previous available day
        :return: A float value or -1.0 if the data is not available (weekend or holiday)
        """
        assert isinstance(d, datetime)
        self.check_empty()
        assert category in {'close', 'open', 'high', 'low'}

        if flexible:
            for i in range(3):  # the market is never out for more than 3 days ??? TODO
                d = d - timedelta(i)
                iso = d.strftime("%Y-%m-%d")
                data_series = self.data.loc[self.data['time'] == iso][category]
                if data_series.empty:
                    continue
                else:
                    return data_series.values[0]

            logger.error(f"Data was not found even after looking backward 3 days\n {str(self.data)}")
            raise ValueError("Data was not found even after looking backward 3 days\n", str(self.data))

        else:
            iso = d.strftime("%Y-%m-%d")
            data_series = self.data.loc[self.data['time'] == iso][category]
            if data_series.empty:
                return -1.0
            else:
                return data_series.values[0]

    def get_rolling_average(self, begin: datetime, end: datetime, category: str = 'close') -> float:
        assert isinstance(begin, datetime) and isinstance(end, datetime)
        assert begin <= end
        self.check_empty()
        assert category in {'close', 'open', 'high', 'low'}

        iso_begin = begin.strftime("%Y-%m-%d")
        iso_end = end.strftime("%Y-%m-%d")
        data_series = self.data.loc[iso_end >= self.data['time'] >= iso_begin][category]
        if data_series.empty:
            return -1.0
        else:

            return sum(data_series.values) / len(data_series.value)