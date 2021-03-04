import unittest
from trade_bot.helpers.order_reconciler import OrderReconciler
from trade_bot.models.Order import Order


class TestOrderReconciler(unittest.TestCase):
    def setUp(self) -> None:
        self.o_r = OrderReconciler(True)

    def tearDown(self) -> None:
        del self.o_r

    def test_return_good_orders(self):
        orders = [
            Order('buy', 'AAPL', 2),
            Order('sell', 'GMC', notional=2000.00),
            Order('buy', 'GOOG', 3.5),
        ]
        new_orders = self.o_r.backtest_orders(orders)

        self.assertTrue(orders == new_orders)

    def test_reduce_multiples(self):
        orders = [
            Order('buy', 'AAPL', 2),
            Order('buy', 'AAPL', 1)
        ]
        resultant = Order('buy', "AAPL", 3)
        filtered = self.o_r.backtest_orders(orders)
        self.assertTrue(resultant == filtered[0])

    def test_reduce_multiples2(self):
        orders = [
            Order('buy', 'AAPL', 2),
            Order('buy', 'AAPL', 1),
            Order('buy', 'AAPL', 5)
        ]
        resultant = Order('buy', "AAPL", 8)
        filtered = self.o_r.backtest_orders(orders)
        self.assertTrue(resultant == filtered[0])

    def test_reduce_multiples3(self):
        orders = [
            Order('buy', 'AAPL', 2),
            Order('buy', 'AAPL', 1),
            Order('sell', 'AAPL', 5)
        ]
        resultant = Order('sell', "AAPL", 2)
        filtered = self.o_r.backtest_orders(orders)
        self.assertTrue(resultant == filtered[0])


if __name__ == '__main__':
    unittest.main()
