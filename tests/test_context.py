import unittest
from models.Context import Context


class TestContext(unittest.TestCase):

    def setUp(self) -> None:
        paper = True
        self.c = Context(paper)

    def tearDown(self) -> None:
        del self.c

    def test_instantiation(self):
        self.assertTrue(True)