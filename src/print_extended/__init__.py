"""
A module to make it easy to use print with pretty formatting.

# Basic usage

```python
from print_extended import print
print("Hello, world!")
```
"""
import sys

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

    def __call__(self, *args, **kwargs):
        file = kwargs.pop("file", self.file)
        self._print(self.group_indent * self.group_level, file=file, end="")
        self._print(file=file, *args, **kwargs)

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


print = Printer()
eprint = Printer(file=sys.stderr)
