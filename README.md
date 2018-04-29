[![PyPi version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPi pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPi license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

Extra functional tools that go beyond standard libraries `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz) and [`fancy`](https://github.com/Suor/funcy).

- This library is under active development, and new functions will be added on regular basis.

## Installation

This package is available on PyPi. Just use `pip3 install -U extratools` to install it.

## Tools

Please check individual source file for details.

### `seqtools`

Tools for sequences.

- `issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

- `issubseqwithgap(a, b)` checks if `a` is a sub-sequence of `b`, where gaps between matching items are allowed.

### `sortedtools`

Tools for sorted sequences.

- `sorteddiff(a, b)` returns the difference between `a` and `b`, where `a` is a super-sequence of `b` with gaps allowed.

## Idea or Contribution

Any idea or contribution is welcome.
