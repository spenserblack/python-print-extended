from io import StringIO
from unittest import TestCase

from src.print_extended import Printer


class TestPrinter(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = StringIO()
        cls.print = Printer(cls.out)

    def tearDown(self):
        self.out.truncate(0)
        self.out.seek(0)

    def test_basic_usage(self):
        """
        It should wrap the builtin print function.
        """
        self.print("Hello, world!")
        self.assertEqual(self.out.getvalue(), "Hello, world!\n")
