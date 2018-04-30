[![PyPi version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPi pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPi license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

Extra functional tools that go beyond standard libraries `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz) and [`fancy`](https://github.com/Suor/funcy).

- Like `toolz`, most of the tools are designed to be efficient, pure, and lazy.

This library is under active development, and new functions will be added on regular basis.

- Any idea or contribution is highly welcome.

## Installation

This package is available on PyPi. Just use `pip3 install -U extratools` to install it.

## Available Tools

Please check individual source file for details.

### [`seqtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

Tools for matching sequences (including strings), with or without gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

- `findsubseq(a, b)` returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

- `issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

- `findsubseqwithgap(a, b)` returns the matching positions where `a` is a sub-sequence of `b`, where gaps are allowed, or `None` when not found.

- `issubseqwithgap(a, b)` checks if `a` is a sub-sequence of `b`, where gaps are allowed.

Tools for comparing sequences (including strings).

- `productcmp(x, y)` compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

    - Throw exception if `x` and `y` have different lengths.

Tools for sorting sequences.

- `sortedbyrank(sth, ranks, reverse=False)` returns the sorted list of `sth`, according to the respective rank of each individual element in `ranks`.

### [`sortedtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

Tools for sorted sequences.

- `sortedcommon(a, b, key=None)` returns the common elements between `a` and `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) & set(b))` but more efficient.

- `sortedalone(a, b, key=None)` returns the elements not in both `a` and `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted((set(a) | set(b)) - (set(a) & set(b)))` but more efficient.

- `sorteddiff(a, b, key=None)` returns the elements only in `a` and not in `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) - set(b))` but more efficient.

- `issubsorted(a, b, key=None)` checks if `a` is a sorted sub-sequence of `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `set(a) <= set(b)` but more efficient.

### [`strtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

Tools for strings.

- `str2grams(s, n, pad=None)` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of string `s`.

    - Optional padding at the start and end can be added by specifying `pad` 

### [`dicttools`](https://github.com/chuanconggao/extratools/blob/master/extratools/dicttools.py)

Tools for inverting dictionaries.

- `invertdict(d)` inverts `(Key, Value)` pairs to `(Value, Key)`.

    - If multiple keys share the same value, the inverted directory keeps last of the respective keys.

- `invertdict_multiple(d)` inverts `(Key, List[Value])` pairs to `(Value, Key)`.

    - If multiple keys share the same value, the inverted directory keeps last of the respective keys.

- `invertdict_safe(d)` inverts `(Key, Value)` pairs to `(Value, List[Key])`.

    - If multiple keys share the same value, the inverted directory keeps a list of all the respective keys.

Tools for remapping elements.

- `remap(data, mapping, key=None)` remaps each unique element in `data` according to function `key`.

    - `mapping` is a dictionary recording all the mappings, optionally containing previous mappings to reuse.

    ``` python
    wordmap = {}
    db = [list(remap(doc, wordmap)) for doc in docs]
    ```

    - In default, `key` returns integers starting from `0`.

### [`settools`](https://github.com/chuanconggao/extratools/blob/master/extratools/settools.py)

Tools for set operations.

- `addtoset(s, x)` checks whether adding `x` to set `s` is successful.

Tools for set similarities.

- `jaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`.

- `multisetjaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two multi-sets (Counters) `a` and `b`.

- `weightedjaccard(a, b, key=sum)` computes the weighted [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`, using function `key` to compute the total weight of the elements within a set.

### [`tabletools`](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

Tools for tables.

- `transpose(m)` returns the transpose of table `m`, i.e., switch rows and columns.

### [`mathtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/mathtools.py)

Tools for math.

- `safediv(a, b)` avoids the `division by zero` exception, by returning infinite with proper sign.

    - Closely referring [IEEE Standard 754](https://en.wikipedia.org/wiki/IEEE_754).

### [`stattools`](https://github.com/chuanconggao/extratools/blob/master/extratools/stattools.py)

Tools for statistics.

- `medianabsdev(data)` computes the [median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation) of a list of floats.

- `entropy(data)` computes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of a list of any items.

    - You can also pass a dictionary of `(item, frequency)` as frequency distribution to `data`.

### [`misctools`](https://github.com/chuanconggao/extratools/blob/master/extratools/misctools.py)

Tools for miscellaneous purposes.

- `cmp(a, b)` restores the useful `cmp` function previously in Python 2.

    - Implemented according to [What's New in Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons).

### [`disjointsets`](https://github.com/chuanconggao/extratools/blob/master/extratools/disjointsets.py)

[Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) with path compression. After `d = DisjointSets()`:

- `d.add(x)` adds a new disjoint set containing `x`.

- `d[x]` returns the representing element of the disjoint set containing `x`.

- `d.disjoints()` returns all the representing elements and their respective disjoint sets.

- `d.union(*xs)` union all the elements in `xs` into a single disjoint set.
