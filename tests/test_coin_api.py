import unittest
from utils.CoinAPI_io import CoinAPI


class TestCoinAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.api = CoinAPI()

    def tearDown(self) -> None:
        del self.api

    def test_initialization(self):
        self.assertTrue(1 == 1)

    def test_good_inputs(self):
        r = self.api.get_daily_data("XRP", stdout=False)
        self.assertTrue(r is not None)

    def test_bad_inputs(self):
        r = self.api.get_daily_data("ADSFAEFA", stdout=False)
        self.assertEqual(None, r)


if __name__ == '__main__':
    unittest.main()