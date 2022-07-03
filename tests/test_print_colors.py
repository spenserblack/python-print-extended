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
            self.ansify(30) + "This is black" + self.ansify(0) + "\nThis is not\n",
        )

    def test_red(self):
        """
        It should color red.
        """
        self.print.red("This is red")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(31) + "This is red" + self.ansify(0) + "\nThis is not\n",
        )

    def test_green(self):
        """
        It should color green.
        """
        self.print.green("This is green")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(32) + "This is green" + self.ansify(0) + "\nThis is not\n",
        )

    def test_yellow(self):
        """
        It should color yellow.
        """
        self.print.yellow("This is yellow")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(33) + "This is yellow" + self.ansify(0) + "\nThis is not\n",
        )

    def test_blue(self):
        """
        It should color blue.
        """
        self.print.blue("This is blue")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(34) + "This is blue" + self.ansify(0) + "\nThis is not\n",
        )

    def test_magenta(self):
        """
        It should color magenta.
        """
        self.print.magenta("This is magenta")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(35) + "This is magenta" + self.ansify(0) + "\nThis is not\n",
        )

    def test_cyan(self):
        """
        It should color cyan.
        """
        self.print.cyan("This is cyan")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(36) + "This is cyan" + self.ansify(0) + "\nThis is not\n",
        )

    def test_white(self):
        """
        It should color white.
        """
        self.print.white("This is white")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(37) + "This is white" + self.ansify(0) + "\nThis is not\n",
        )

    def test_rgb(self):
        """
        It should add RGB true colors.
        """
        self.print.rgb(255, 127, 255)("This is pinkish purple")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(38, 2, 255, 127, 255)
            + "This is pinkish purple"
            + self.ansify(0)
            + "\nThis is not\n",
        )

    def test_on_black(self):
        """
        It should color the background black.
        """
        self.print.on_black("This is on black")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(40) + "This is on black" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_red(self):
        """
        It should color the background red.
        """
        self.print.on_red("This is on red")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(41) + "This is on red" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_green(self):
        """
        It should color the background green.
        """
        self.print.on_green("This is on green")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(42) + "This is on green" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_yellow(self):
        """
        It should color the background yellow.
        """
        self.print.on_yellow("This is on yellow")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(43) + "This is on yellow" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_blue(self):
        """
        It should color the background blue.
        """
        self.print.on_blue("This is on blue")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(44) + "This is on blue" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_magenta(self):
        """
        It should color the background magenta.
        """
        self.print.on_magenta("This is on magenta")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(45) + "This is on magenta" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_cyan(self):
        """
        It should color the background cyan.
        """
        self.print.on_cyan("This is on cyan")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(46) + "This is on cyan" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_white(self):
        """
        It should color the background white.
        """
        self.print.on_white("This is on white")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(47) + "This is on white" + self.ansify(0) + "\nThis is not\n",
        )

    def test_on_rgb(self):
        """
        It should add RGB true colors to the background.
        """
        self.print.on_rgb(255, 127, 255)("This is pinkish purple")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(48, 2, 255, 127, 255)
            + "This is pinkish purple"
            + self.ansify(0)
            + "\nThis is not\n",
        )
