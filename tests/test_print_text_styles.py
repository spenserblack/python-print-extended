from . import PrinterTestCase


class TestTextStyles(PrinterTestCase):
    """
    Test suite for styled outputs.
    """

    def test_bold(self):
        """
        It should style bold.
        """
        self.print.bold("This is bold")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(1) + "This is bold" + self.ansify(0) + "\nThis is not\n",
        )

    def test_italic(self):
        """
        It should style italic.
        """
        self.print.italic("This is italic")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(3) + "This is italic" + self.ansify(0) + "\nThis is not\n",
        )

    def test_underline(self):
        """
        It should style underline.
        """
        self.print.underline("This is underline")
        self.print("This is not")
        self.assertEqual(
            self.out.getvalue(),
            self.ansify(4) + "This is underline" + self.ansify(0) + "\nThis is not\n",
        )
