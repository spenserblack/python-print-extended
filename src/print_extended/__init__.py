"""
A module to make it easy to use print with pretty formatting.

# Basic usage

```python
from print_extended import print
print("Hello, world!")
```
"""
import sys

__all__ = ["Printer", "print", "eprint"]


class Printer:
    """
    A class to make it easy to use print with pretty formatting.
    """

    _print = print

    def __init__(self, file=sys.stdout):
        """
        Initialize the printer.

        # Args

        - `file`: The file to print to.
        """
        self.file = file

    def __call__(self, *args, **kwargs):
        file = kwargs.pop("file", self.file)
        return self._print(file=file, *args, **kwargs)


print = Printer()
eprint = Printer(file=sys.stderr)
