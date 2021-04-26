import unittest
from pandas import DataFrame as df
from models.BarsData import BarsData


class TestBarsData(unittest.TestCase):

    def test_instantiation(self):
        bd = BarsData("AAPL")