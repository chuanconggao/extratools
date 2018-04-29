[![PyPi version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPi pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPi license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

Extra functional tools that go beyond standard libraries `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz) and [`fancy`](https://github.com/Suor/funcy).

- This library is under active development, and new functions will be added on regular basis.

- Any idea or contribution is highly welcome.

## Installation

This package is available on PyPi. Just use `pip3 install -U extratools` to install it.

## Available Tools

Please check individual source file for details.

### [`seqtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

Tools for sequences (including strings).

- `findsubseq(a, b)` returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

- `issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

- `findsubseqwithgap(a, b)` returns the matching positions where `a` is a sub-sequence of `b`, where gaps between matching items are allowed, or `[]` when not found.

- `issubseqwithgap(a, b)` checks if `a` is a sub-sequence of `b`, where gaps between matching items are allowed.

- `productcmp(x, y)` compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

- `sortedbyrank(sth, ranks, reverse=False)` returns the sorted list of `sth`, according to the respective rank of each individual element in `ranks`.

### [`sortedtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

Tools for sorted sequences.

- `sorteddiff(a, b)` returns the difference between `a` and `b`, where `a` is a super-sequence of `b` with gaps allowed.

### [`strtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

Tools for strings.

- `str2grams(s, n)` returns the ordered `n`-grams of string `s`.

### [`settools`](https://github.com/chuanconggao/extratools/blob/master/extratools/settools.py)

Tools for sets.

- `addtoset(s, x)` checks whether adding `x` to set `s` is successful.

- `jaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`.

- `weightedjaccard(a, b, key=sum)` computes the weighted [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`, using function `key` to compute the total weight of the elements within a set.

### [`tabletools`](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

Tools for tables.

- `transpose(m)` returns the transpose of table `m`, i.e., switch rows and columns.

### [`mathtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/mathtools.py)

Tools for math.

- `safediv(a, b)` avoids the `division by zero` exception, by returning infinite with proper sign, closely referring [IEEE Standard 754](https://en.wikipedia.org/wiki/IEEE_754).

### [`misctools`](https://github.com/chuanconggao/extratools/blob/master/extratools/misctools.py)

Tools for miscellaneous purposes.

- `cmp(a, b)` restores the useful `cmp` function previously in Python 2, according to [What's New in Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons).
