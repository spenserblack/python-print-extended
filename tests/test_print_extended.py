import sty

from . import PrinterTestCase


class TestPrinter(PrinterTestCase):
    def test_basic_usage(self):
        """
        It should wrap the builtin print function.
        """
        self.print("Hello, world!")
        self.assertEqual(self.out.getvalue(), "Hello, world!\n")

    def test_grouping(self):
        """
        It should create groups.
        """
        self.print("no group")
        self.print.group()
        self.print("group 1")
        self.print("group 1 line 2")
        self.print.group()
        self.print("group 2")
        self.print.endgroup()
        self.print.endgroup()
        self.print("no group")

        self.assertEqual(
            self.out.getvalue().splitlines(),
            [
                "no group",
                "    group 1",
                "    group 1 line 2",
                "        group 2",
                "no group",
            ],
        )


class TestColors(PrinterTestCase):
    """
    Test suite for colored outputs.
    """

    def test_red(self):
        """
        It should color red.
        """
        self.print.red("This is red")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.red + "This is red\n" + sty.ef.rs + "This is not\n",
        )
