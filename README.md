# print-extended

[![CI](https://github.com/spenserblack/python-print-extended/actions/workflows/ci.yml/badge.svg)](https://github.com/spenserblack/python-print-extended/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/spenserblack/python-print-extended/branch/main/graph/badge.svg?token=tgIB3T966J)](https://codecov.io/gh/spenserblack/python-print-extended)

An extended version of the print function.

The intent is to make it easy to print pretty outputs, with an interface
that Python beginners who just made their first "Hello World" can use.

You can always use `pprint`, `sys.stderr`, etc., and probably should for
complex usage. As stated, this is to be beginner-friendly. Functionality
will be sacrificed for ease-of-use.

## Features

- `print.group` and `print.endgroup` to create indentation levels
- foreground colors
  - `print.red('foo')`
  - `print.green('foo')`
  - `print.blue('foo')`
  - `print.yellow('foo')`
  - `print.magenta('foo')`
  - `print.cyan('foo')`
  - `print.rgb(r, g, b)('foo')`
- background colors
  - `print.on_red('foo')`
  - `print.on_green('foo')`
  - `print.on_blue('foo')`
  - `print.on_yellow('foo')`
  - `print.on_magenta('foo')`
  - `print.on_cyan('foo')`
  - `print.on_rgb(r, g, b)('foo')`
- text styles
  - `print.bold('foo')`
  - `print.italic('foo')`
  - `print.underline('foo')`
  - Also chainable! `print.red.bold.italic('error')`
- `eprint` to simplify printing to STDERR

## Development

```bash
# Activate virtual environment
python -m pip install -U pip
python -m pip install .
python -m pip install -r requirements-dev.txt
pre-commit install
```
