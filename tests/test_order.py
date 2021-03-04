import unittest
from trade_bot.models.Order import Order


class TestOrder(unittest.TestCase):

    def test_instantiation(self):
        try:
            Order('buy', "GMC", 2)
            Order('sell', 'RKT', notional=1500.00)
            Order("buy", "AMC", notional=1000.00)
        except AssertionError:
            self.fail()
        else:
            self.assertTrue(True)

    def test_bad_orders(self):
        orders = [
            ("hold", "BTC"),
            ("SELL", 'GMC', 2.0),
            ("buy", "AAPL", 2.0, 'stop_limit'),

        ]
        for o in orders:
            try:
                Order(*o)
            except AssertionError:
                continue
            else:
                self.fail()




if __name__ == '__main__':
    unittest.main()
