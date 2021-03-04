import unittest
from trade_bot.models.Algo import Algorithm


class TestAlgo(unittest.TestCase):

    def test_instantiation(self):
        created = False
        try:
            obj = Algorithm()
        except NotImplementedError:
            pass
        else:
            created = True

        self.assertTrue(created)

    def test_no_implement_func(self):
        ran = False
        try:
            obj = Algorithm()
            obj.before_trading()
        except NotImplementedError:
            pass
        else:
            created = True

        self.assertFalse(ran)


if __name__ == '__main__':
    unittest.main()
