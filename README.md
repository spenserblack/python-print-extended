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
- colored/styled prints
  - `print.red('foo')`
  - `print.green('foo')`
  - `print.blue('foo')`
  - `print.yellow('foo')`
  - `print.magenta('foo')`
  - `print.cyan('foo')`
  - `print.rgb(r, g, b)('foo')`
  - `print.bold('foo')`
  - `print.italic('foo')`
  - `print.underline('foo')`
  - Also chainable! `print.red.bold.italic('error')`
- `eprint` to simplify printing to STDERR
