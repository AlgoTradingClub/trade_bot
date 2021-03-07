from trade_bot.utils.CoinGeckoData import CoinGecko
import unittest


class TestCoinAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.api = CoinGecko()

    def tearDown(self) -> None:
        del self.api

    def test_initialization(self):
        self.assertTrue(1 == 1)

    def test_get_curr_price(self):
        resp = self.api.get_price('bitcoin', 'usd')
        self.assertTrue(resp)

    def test_get_curr_price(self):
        resp = self.api.get_price('bitcoin', 'usd')
        self.assertTrue(resp)

    def test_get_historical_data(self):
        resp = self.api.get_historical_data('bitcoin')


if __name__ == '__main__':
    unittest.main()