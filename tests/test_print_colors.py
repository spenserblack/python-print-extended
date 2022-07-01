import sty

from . import PrinterTestCase


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
            sty.fg.black + "This is black\n" + sty.rs.all + "This is not\n",
        )

    def test_red(self):
        """
        It should color red.
        """
        self.print.red("This is red")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.red + "This is red\n" + sty.rs.all + "This is not\n",
        )

    def test_green(self):
        """
        It should color green.
        """
        self.print.green("This is green")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.green + "This is green\n" + sty.rs.all + "This is not\n",
        )

    def test_blue(self):
        """
        It should color blue.
        """
        self.print.blue("This is blue")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.blue + "This is blue\n" + sty.rs.all + "This is not\n",
        )

    def test_yellow(self):
        """
        It should color yellow.
        """
        self.print.yellow("This is yellow")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.yellow + "This is yellow\n" + sty.rs.all + "This is not\n",
        )

    def test_magenta(self):
        """
        It should color magenta.
        """
        self.print.magenta("This is magenta")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.magenta + "This is magenta\n" + sty.rs.all + "This is not\n",
        )

    def test_cyan(self):
        """
        It should color cyan.
        """
        self.print.cyan("This is cyan")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.cyan + "This is cyan\n" + sty.rs.all + "This is not\n",
        )

    def test_white(self):
        """
        It should color white.
        """
        self.print.white("This is white")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.white + "This is white\n" + sty.rs.all + "This is not\n",
        )

    def test_rgb(self):
        """
        It should add RGB true colors.
        """
        self.print.rgb(255, 127, 255)("This is pinkish purple")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            sty.fg.rgb_call(255, 127, 255)
            + "This is pinkish purple\n"
            + sty.rs.all
            + "This is not\n",
        )
