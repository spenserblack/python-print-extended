# print-extended

[![CI](https://github.com/spenserblack/python-print-extended/actions/workflows/ci.yml/badge.svg)](https://github.com/spenserblack/python-print-extended/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/spenserblack/python-print-extended/branch/main/graph/badge.svg?token=tgIB3T966J)](https://codecov.io/gh/spenserblack/python-print-extended)

An extended version of the print function.

The intent is to make it easy to print pretty outputs, with an interface
that Python beginners who just made their first "Hello World" can use.

You can always use `pprint`, `sys.stderr`, etc., and probably should for
complex usage. As stated, this is to be beginner-friendly.

## Features

- `print.group` and `print.endgroup` to create indentation levels
- colored prints
  - `print.red('foo')`
  - `print.green('foo')`
  - `print.blue('foo')`
  - `print.yellow('foo')`
  - `print.magenta('foo')`
  - `print.cyan('foo')`
  - `print.rgb(r, g, b)('foo')`
- `print.info` (same as `print` by default, but can be used by a `print.logger`)
- `print.err` and `print.warn` that will attempt to style outputs red and yellow, respectively
- `eprint` to simplify printing to STDERR
- `print.prefix` to build a printer with a prefix (e.g `[LEVEL] TIMESTAMP MESSAGE`)
