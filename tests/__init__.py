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

    @staticmethod
    def ansify(*args):
        return f"\x1B[{';'.join(str(arg) for arg in args)}m"
