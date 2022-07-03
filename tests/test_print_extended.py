from src.print_extended import NoGroupError

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

    def test_extra_endgroup(self):
        """
        It should raise an error if an endgroup is called without a group.
        """
        with self.assertRaises(NoGroupError):
            self.print.endgroup()
