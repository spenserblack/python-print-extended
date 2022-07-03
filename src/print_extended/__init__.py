"""
A module to make it easy to use print with pretty formatting.

# Basic usage

```python
from print_extended import print
print("Hello, world!")
```
"""
import sys

# TODO Remove sty dependency?
import sty

__all__ = ["Printer", "print", "eprint", "NoGroupError"]


class NoGroupError(Exception):
    """
    Raised when the user attempts to end a group without starting one.
    """

    def __init__(self):
        super().__init__("Cannot end a group without starting one.")


class Printer:
    """
    A class to make it easy to use print with pretty formatting.
    """

    _print = print

    def __init__(self, group_indent="    ", file=sys.stdout):
        """
        Initialize the printer.

        # Args

        - `group_indent`: The indentation for each group of items.
        - `file`: The file to print to.
        """
        self.file = file
        self.group_indent = group_indent
        self.group_level = 0
        self._sty = []

    def __call__(self, *args, **kwargs):
        file = kwargs.pop("file", self.file)
        end = kwargs.pop("end", "\n")
        self._print(self.group_indent * self.group_level, file=file, end="")
        self._print(*self._sty, file=file, end="", sep="")
        self._print(file=file, end="", *args, **kwargs)
        if len(self._sty) > 0:
            self._print(sty.rs.all, file=file, end=end)
        else:
            self._print(file=file, end=end)

    def group(self):
        """
        Starts a group by increasing the indentation level.
        """
        self.group_level += 1

    def endgroup(self):
        """
        Ends a group by decreasing the indentation level.
        """
        if self.group_level == 0:
            raise NoGroupError()
        self.group_level -= 1

    @property
    def black(self):
        """
        Returns a printer with the foreground color set to black.
        """
        return self._apply_fg("black")

    @property
    def on_black(self):
        """
        Returns a printer with the background color set to black.
        """
        return self._apply_bg("black")

    @property
    def red(self):
        """
        A printer that prints red text.
        """
        return self._apply_fg("red")

    @property
    def on_red(self):
        """
        Returns a printer with the background color set to red.
        """
        return self._apply_bg("red")

    @property
    def green(self):
        """
        A printer that prints green text.
        """
        return self._apply_fg("green")

    @property
    def on_green(self):
        """
        Returns a printer with the background color set to green.
        """
        return self._apply_bg("green")

    @property
    def blue(self):
        """
        A printer that prints blue text.
        """
        return self._apply_fg("blue")

    @property
    def on_blue(self):
        """
        Returns a printer with the background color set to blue.
        """
        return self._apply_bg("blue")

    @property
    def yellow(self):
        """
        A printer that prints yellow text.
        """
        return self._apply_fg("yellow")

    @property
    def on_yellow(self):
        """
        Returns a printer with the background color set to yellow.
        """
        return self._apply_bg("yellow")

    @property
    def magenta(self):
        """
        A printer that prints magenta text.
        """
        return self._apply_fg("magenta")

    @property
    def on_magenta(self):
        """
        Returns a printer with the background color set to magenta.
        """
        return self._apply_bg("magenta")

    @property
    def cyan(self):
        """
        A printer that prints cyan text.
        """
        return self._apply_fg("cyan")

    @property
    def on_cyan(self):
        """
        Returns a printer with the background color set to cyan.
        """
        return self._apply_bg("cyan")

    @property
    def white(self):
        """
        A printer that prints white text.
        """
        return self._apply_fg("li_grey")

    @property
    def on_white(self):
        """
        Returns a printer with the background color set to white.
        """
        return self._apply_bg("li_grey")

    def rgb(self, r, g, b):
        """
        A printer that prints text with the given RGB color.
        """
        p = self._copy()
        p._sty.append(sty.fg.rgb_call(r, g, b))
        return p

    def on_rgb(self, r, g, b):
        """
        Returns a printer with the background color set to the given RGB color.
        """
        p = self._copy()
        p._sty.append(sty.bg.rgb_call(r, g, b))
        return p

    @property
    def bold(self):
        """
        A printer that prints bold text.
        """
        return self._apply_style("bold")

    @property
    def underline(self):
        """
        A printer that prints underlined text.
        """
        return self._apply_style("underl")

    @property
    def italic(self):
        """
        A printer that prints italic text.
        """
        return self._apply_style("italic")

    def _apply_fg(self, fg):
        """
        Applies a foreground color to a new printer.
        """
        p = self._copy()
        p._sty.append(getattr(sty.fg, fg))
        return p

    def _apply_bg(self, bg):
        """
        Applies a background color to a new printer.
        """
        p = self._copy()
        p._sty.append(getattr(sty.bg, bg))
        return p

    def _apply_style(self, style):
        """
        Applies a style to a new printer.
        """
        p = self._copy()
        p._sty.append(getattr(sty.ef, style))
        return p

    def _copy(self):
        """
        Creates a new printer with the same settings.
        """
        p = Printer(self.group_indent, self.file)
        p._sty = self._sty.copy()
        p.group_level = self.group_level
        return p


print = Printer()
eprint = Printer(file=sys.stderr)
