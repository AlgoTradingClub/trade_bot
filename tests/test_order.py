import unittest
from models.Order import Order


class TestOrder(unittest.TestCase):

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

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

    def test_condense(self):
        orders = [
            ("buy", "GMC", 2.5),
            ("buy", 'GMC', 3.0),
        ]
        objs = [Order(*o) for o in orders]

        self.assertTrue(objs[0].condensable(objs[1]))

    def test_condense2(self):
        orders = [
            ("buy", "GMC", 2.5),
            ("sell", 'GMC', 3.0),
        ]
        objs = [Order(*o) for o in orders]

        self.assertTrue(objs[0].condensable(objs[1]))

    def test_condense3(self):
        orders = [
            ("buy", "GMC", 2.5),
            ("buy", 'GMC', 3.0, 'limit', 0.0, 'day', 150.0),
        ]
        objs = [Order(*o) for o in orders]

        self.assertFalse(objs[0].condensable(objs[1]))


if __name__ == '__main__':
    unittest.main()
