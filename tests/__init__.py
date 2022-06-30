from io import StringIO
from unittest import TestCase

from src.print_extended import Printer


class PrinterTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = StringIO()
        cls.print = Printer(file=cls.out)

    def tearDown(self):
        self.out.truncate(0)
        self.out.seek(0)
