import unittest
from utils.CoinAPI_io import CoinAPI


class TestCoinAPI(unittest.TestCase):

    def test_initialization(self):
        CoinAPI()
        self.assertTrue(1 == 1)


if __name__ == '__main__':
    unittest.main()