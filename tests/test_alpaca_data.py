import unittest
from utils.Alpaca_Data import AlpacaData


class TestAlpacaData(unittest.TestCase):

    def setUp(self) -> None:
        self.a = AlpacaData()

    def tearDown(self) -> None:
        del self.a

    def test_no_key_id(self):
        try:
            self.a.key_id
        except AttributeError:
            self.assertTrue(True)
        else:
            self.fail("Did not delete the key id")

    def test_no_secret_key(self):
        try:
            self.a.secret_key
        except AttributeError:
            self.assertTrue(True)
        else:
            self.fail("Did not delete the secret key")

    def test_get_data(self):
        stonks = ["AAPL", "GMC", "AMC"]
        data = self.a.get_bars_data(stonks, limit=2)
        self.assertTrue(isinstance(data[stonks[0]]['high'][0], float))
        self.assertTrue(len(data) == len(stonks))


if __name__ == '__main__':
    unittest.main()