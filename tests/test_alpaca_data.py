import unittest
from trade_bot.utils.Alpaca_Data import AlpacaData


class TestAlpacaData(unittest.TestCase):

    def test_no_key_id(self):
        a = AlpacaData()
        try:
            a.key_id
        except AttributeError:
            self.assertTrue(True)
        else:
            self.fail("Did not delete the key id")

    def test_no_secret_key(self):
        a = AlpacaData()
        try:
            a.secret_key
        except AttributeError:
            self.assertTrue(True)
        else:
            self.fail("Did not delete the secret key")

    def test_get_assets(self):
        a = AlpacaData()
        stuff = a.list_assets()
        self.assertTrue(isinstance(stuff, list))

    def test_get_data(self):
        a = AlpacaData()
        stonks = ["AAPL", "GMC", "AMC"]
        data = a.get_bars_data(stonks, limit=2)
        self.assertTrue(isinstance(data[stonks[0]]['high'][0], float))
        self.assertTrue(len(data) == len(stonks))


if __name__ == '__main__':
    unittest.main()