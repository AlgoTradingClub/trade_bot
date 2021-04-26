import unittest
from models.Data import Data
from pandas import DataFrame as df


class TestData(unittest.TestCase):

    def test_instantiation(self):
        d = Data("AAPL", df())
        self.assertTrue(True)

    def test_instantiation_bad(self):
        try:
            d = Data()
        except TypeError:
            self.assertTrue(True)

    def test_instantiation_bad2(self):
        try:
            d = Data("AAPL", [])
        except ValueError:
            self.assertTrue(True)

