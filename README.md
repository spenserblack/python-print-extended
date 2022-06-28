# print-extended

An extended version of the print function.

The intent is to make it easy to print pretty outputs with an interface
that Python beginners who just made their first "Hello World" can use.

You can always use `pprint`, `sys.stderr`, etc., and probably should for
complex usage. As stated, this is to be beginner-friendly.

## Features

- `print.group` and `print.endgroup` to create indentation levels
- `print.info` (same as `print` by default, but can be used by a `print.logger`)
- `print.err` and `print.warn` that will attempt to style outputs red and yellow, respectively
- `eprint` to simplify printing to STDERR
- `print.logger` to build a printer with a prefix (defaults to `[LEVEL] TIMESTAMP MESSAGE`)
  - ```python
    # Example
    logger = print.logger()
    logger.info('Hello World')
    # [INFO] 2022/01/01 13:00:00 - Hello World
    ```
