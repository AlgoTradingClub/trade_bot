import unittest
from trade_bot.utils.CoinAPI_io import CoinAPI


class TestCoinAPI(unittest.TestCase):

    def test_initialization(self):
        api = CoinAPI()
        self.assertTrue(1 == 1)

    def test_good_inputs(self):
        api = CoinAPI()
        r = api.get_daily_data("XRP", stdout=False)
        self.assertTrue(r is not None)

    def test_bad_inputs(self):
        api = CoinAPI()
        r = api.get_daily_data("ADSFAEFA", stdout=False)
        self.assertEqual(None, r)


if __name__ == '__main__':
    unittest.main()