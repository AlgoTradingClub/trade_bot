import unittest
from trade_bot.models.Algo import Algorithm


class TestAlgo(unittest.TestCase):

    def setUp(self) -> None:
        self.a = Algorithm()

    def tearDown(self) -> None:
        del self.a

    def test_no_implement_func(self):
        ran = False
        try:
            self.a = Algorithm()
            self.a.before_trading()
        except NotImplementedError:
            pass
        else:
            created = True

        self.assertFalse(ran)


if __name__ == '__main__':
    unittest.main()
