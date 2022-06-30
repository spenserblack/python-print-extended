import sty

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


class TestColors(PrinterTestCase):
    """
    Test suite for colored outputs.
    """

    def test_black(self):
        """
        It should color black.
        """
        self.print.black("This is black")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.black + "This is black\n" + sty.ef.rs + "This is not\n",
        )

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

    def test_green(self):
        """
        It should color green.
        """
        self.print.green("This is green")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.green + "This is green\n" + sty.ef.rs + "This is not\n",
        )

    def test_blue(self):
        """
        It should color blue.
        """
        self.print.blue("This is blue")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.blue + "This is blue\n" + sty.ef.rs + "This is not\n",
        )

    def test_yellow(self):
        """
        It should color yellow.
        """
        self.print.yellow("This is yellow")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.yellow + "This is yellow\n" + sty.ef.rs + "This is not\n",
        )

    def test_magenta(self):
        """
        It should color magenta.
        """
        self.print.magenta("This is magenta")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.magenta + "This is magenta\n" + sty.ef.rs + "This is not\n",
        )

    def test_cyan(self):
        """
        It should color cyan.
        """
        self.print.cyan("This is cyan")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.cyan + "This is cyan\n" + sty.ef.rs + "This is not\n",
        )

    def test_white(self):
        """
        It should color white.
        """
        self.print.white("This is white")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.white + "This is white\n" + sty.ef.rs + "This is not\n",
        )
