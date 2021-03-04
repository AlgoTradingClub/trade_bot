import unittest
from trade_bot.utils.Alpaca_Account import AlpacaAccount


class TestAlpacaData(unittest.TestCase):

    def setUp(self) -> None:
        self.a = AlpacaAccount()

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

    def test_get_assets(self):
        stuff = self.a.list_assets()
        self.assertTrue(isinstance(stuff, list))


if __name__ == '__main__':
    unittest.main()