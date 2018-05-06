[![PyPI version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

Extra functional tools that go beyond standard library's `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz), [`fancy`](https://github.com/Suor/funcy), and [`more-itertools`](https://github.com/erikrose/more-itertools).

- Like `toolz` and others, most of the tools are designed to be efficient, pure, and lazy. Several useful yet non-functional tools are also included.

- While `toolz` and others target basic scenarios, most tools in this library target more advanced and complete scenarios.

- A few useful CLI tools for respective functions are also installed. They are available as `extratools-[funcname]`.

This library is under active development, and new functions will be added on regular basis.

- Any idea or contribution is highly welcome.

- Currently adopted by [TopSim](https://github.com/chuanconggao/TopSim) and [PrefixSpan-py](https://github.com/chuanconggao/PrefixSpan-py).

# Installation

This package is available on PyPI. Just use `pip3 install -U extratools` to install it.

# Examples

Here are three examples out of dozens of our tools.

- `seqtools.compress(data, key=None)` compresses the sequence by encoding continuous identical `Item` to `(Item, Count)`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

- `rangetools.gaps(covered, whole=(-inf, inf))` computes the uncovered ranges of the whole range `whole`, given the covered ranges `covered`.

``` python
list(gaps(
    [(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)],
    (0, 1)
))
# [(0, 0.1), (0.2, 0.5), (0.9, 1)]
```

- `jsontools.flatten(data, force=False)` flattens a JSON object by returning `(Path, Value`) tuples with each path `Path` from root to each value `Value`.

``` python
flatten(json.loads("""{
  "name": "John",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}"""))
# {'name': 'John',
#  'address.streetAddress': '21 2nd Street',
#  'address.city': 'New York',
#  'phoneNumbers[0].type': 'home',
#  'phoneNumbers[0].number': '212 555-1234',
#  'phoneNumbers[1].type': 'office',
#  'phoneNumbers[1].number': '646 555-4567',
#  'children': [],
#  'spouse': None}
```

# Index of All Tools

Functions:

[`seqtools`](#seqtools)
[`sortedtools`](#sortedtools)
[`strtools`](#strtools)
[`rangetools`](#rangetools)
[`dicttools`](#dicttools)
[`jsontools`](#jsontools)
[`settools`](#settools)
[`tabletools`](#tabletools)
[`mathtools`](#mathtools)
[`stattools`](#stattools)
[`misctools`](#misctools)
[`printtools`](#printtools)
[`debugtools`](#debugtools)

Data Structures:

[`disjointsets`](#disjointsets)
[`defaultlist`](#defaultlist)

CLI Tools:

[`dicttools.remap`](#dicttools)
[`jsontools.flatten`](#jsontools)
[`stattools.teststats`](#stattools)

## Functions

<a name="seqtools"></a>
### [`seqtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

Tools for matching sequences (including strings), with or without gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

- `findsubseq(a, b)` returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

- `issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

- `findsubseqwithgap(a, b)` returns the matching positions where `a` is a sub-sequence of `b`, where gaps are allowed, or `None` when not found.

- `issubseqwithgap(a, b)` checks if `a` is a sub-sequence of `b`, where gaps are allowed.

- `nextentries` is alias of a tool in `dicttools`.

- `align(a, b, cost=None, bound=inf, default=None)` [aligns](https://en.wikipedia.org/wiki/Sequence_alignment) two sequences `a` and `b`, such that the total cost of the aligned sequences given the pair-wise cost function `cost(x, y)` is minimized.

    - Assume the aligned sequences are `a'` and `b'`. The total cost is `sum(cost(x, y) for x, y in zip(a', b'))`.

    - Both the minimum total cost and the respective aligned sequences are returned as a tuple.

    - In default, the cost function `cost(x, y)` returns `1` when `x == y` and `0` when not. This is equal to the [edit distance](https://en.wikipedia.org/wiki/Edit_distance).

    - To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

``` python
align(
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1]
)
# (2, ([0, None, 1, 1, 0,    1],
#      [0, 0,    1, 1, None, 1]))

align(
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    bound=1
)
# None
```

Tools for comparing sequences (including strings).

- `productcmp(x, y)` compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

    - Throw exception if `x` and `y` have different lengths.

Tools for sorting sequences.

- `sortedbyrank(data, ranks, reverse=False)` returns the sorted list of `data`, according to the respective rank of each individual element in `ranks`.

Tools for encoding/decoding sequences.

- `compress(data, key=None)` compresses the sequence by encoding continuous identical `Item` to `(Item, Count)`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

    - Different from [`itertools.compress`](https://docs.python.org/3.6/library/itertools.html#itertools.compress).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

- `decompress(data)` decompresses the sequence by decoding `(Item, Count)` to continuous identical `Item`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

- `todeltas(data, op=operator.sub)` compresses the sequence by encoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

    - For custom type of item, either define the `-` operator or specify the `op` function computing the difference.

``` python
list(todeltas([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
```

- `fromdeltas(data, op=operator.add)` decompresses the sequence by decoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

    - For custom type of item, either define the `+` operator or specify the `op` function merging the difference.

Tools for joining sequences.

- `join(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)` joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

    - If both two sequences are sorted according to `leftkey` and `rightkey`, respectively, then optimized `sortedtools.join` with the same API should be used for better efficiency.

    - Unlike `sortedtools.join`, `join` is just a wrapper of `toolz.itertools.join` with a slightly more friendly API.

<a name="sortedtools"></a>
### [`sortedtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

Tools for joining sorted sequences.

- `sortedjoin(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)` joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

    - Two sequences must be already sorted according to `leftkey` and `rightkey`, respectively.

    - `sortedjoin` is completely lazy, and more efficient than `seqtools.join` and its underneath `toolz.itertools.join`.

``` python
list(sortedjoin([-1, -1, -2, -4, -5, -6], [0, 1, 1, 2, 3, 4, 5, 5], leftkey=abs, leftdefault=None))
# [(None, 0),
#  (-1, 1),
#  (-1, 1),
#  (-1, 1),
#  (-1, 1),
#  (-2, 2),
#  (None, 3),
#  (-4, 4),
#  (-5, 5),
#  (-5, 5)]
```

Tools for matching sorted sequences.

- `sortedcommon(a, b, key=None)` returns the common elements between `a` and `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) & set(b))` but more efficient.

- `sortedalone(a, b, key=None)` returns the elements not in both `a` and `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted((set(a) | set(b)) - (set(a) & set(b)))` but more efficient.

- `sorteddiff(a, b, key=None)` returns the elements only in `a` and not in `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) - set(b))` but more efficient.

- `issubsorted(a, b, key=None)` checks if `a` is a sorted sub-sequence of `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `set(a) <= set(b)` but more efficient.

<a name="strtools"></a>
### [`strtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

Tools for string transformations.

- `str2grams(s, n, pad=None)` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of string `s`.

    - Optional padding at the start and end can be added by specifying `pad`. `\0` is usually a safe choice for `pad` when not displaying.

Tools for checksums.

- `sha1sum(f)`, `sha256sum(f)`, `sha512sum(f)`, `md5sum(f)` compute the respective checksum, accepting string, bytes, text file object, and binary file object.

Tools for string matching.

- `tagstats(tags, lines, separator=None)` efficiently computes the number of lines containing each tag.

    - [TagStats](https://github.com/chuanconggao/TagStats) is used to compute efficiently, where the common prefixes among tags are matched only once.

    - `separator` is a regex to tokenize each string. In default when `separator` is `None`, each string is not tokenized.

``` python
tagstats(
    ["a b", "a c", "b c"],
    ["a b c", "b c d", "c d e"]
)
# {'a b': 1, 'a c': 0, 'b c': 2}
```

- `editdist(a, b, bound=inf)` computes the [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between two strings `a` and `b`.

    - To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

``` python
editdist("dog", "frog")
# 2
```

<a name="rangetools"></a>
### [`rangetools`](https://github.com/chuanconggao/extratools/blob/master/extratools/rangetools.py)

Tools for statistics over ranges. Note that each range is closed on the left side, and open on the right side.

- `histogram(thresholds, data, leftmost=-inf)` computes the [histogram](https://en.wikipedia.org/wiki/Histogram) over all the floats in `data`.

    - The search space is divided by the thresholds of bins specified in `thresholds`.

    - Each bin of the histogram is labelled by its lower threshold.

        - All values in the bin are no less than the current threshold and less than the next threshold.

        - The first bin is labelled by `leftmost`, which is `-inf` in default.

``` python
histogram(
    [0.1, 0.5, 0.8, 0.9],
    [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
)
# {-inf: 1, 0.1: 4, 0.5: 3, 0.8: 1, 0.9: 2}
```

Tools for querying ranges.

- `rangequery(keyvalues, query, func=min)` finds the best value from the covered values in `keyvalues`, if each key in `keyvalues` is within the query range `query`.

    - Implemented by [RangeMinQuery](https://github.com/chuanconggao/RangeMinQuery) to solve the [range minimum query](https://en.wikipedia.org/wiki/Range_minimum_query) problem.

    - `func` defines how the best value is computed, and defaults to `min` for minimum value.

``` python
rangequery(
    {0.1: 1, 0.2: 3, 0.3: 0},
    (0.2, 0.4)
)
# 0
```

Tools for transformations over ranges. Note that each range is closed on the left side, and open on the right side.

- `covers(covered)` merges the covered ranges `covered` to resolve any overlap.

    - Covered ranges in `covered` are sorted by the left side of each range.

``` python
list(covers([(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)]))
# [(-inf, 0), (0.1, 0.2), (0.5, 0.9)]
```

- `gaps(covered, whole=(-inf, inf))` computes the uncovered ranges of the whole range `whole`, given the covered ranges `covered`.

    - Covered ranges in `covered` are sorted by the left side of each range.

    - Overlaps among covered ranges `covered` are resolved, like `covers(covered)`.

``` python
list(gaps(
    [(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)],
    (0, 1)
))
# [(0, 0.1), (0.2, 0.5), (0.9, 1)]
```

<a name="dicttools"></a>
### [`dicttools`](https://github.com/chuanconggao/extratools/blob/master/extratools/dicttools.py)

Tools for inverting dictionaries.

- `invert(d)` inverts `(Key, Value)` pairs to `(Value, Key)`.

    - If multiple keys share the same value, the inverted directory keeps last of the respective keys.

- `invert_multiple(d)` inverts `(Key, List[Value])` pairs to `(Value, Key)`.

    - If multiple keys share the same value, the inverted directory keeps last of the respective keys.

- `invert_safe(d)` inverts `(Key, Value)` pairs to `(Value, List[Key])`.

    - If multiple keys share the same value, the inverted directory keeps a list of all the respective keys.

Tools for remapping elements.

- `remap(data, mapping, key=None)` remaps each unique element in `data` according to function `key`.

    - `mapping` is a dictionary recording all the mappings, optionally containing previous mappings to reuse.

    - In default, `key` returns integers starting from `0`.

``` python
wordmap = {}
db = [list(remap(doc, wordmap)) for doc in docs]
```

Tools for indexing.

- `invertedindex(seqs)` creates an [inverted index](https://en.wikipedia.org/wiki/Inverted_index).

    - Each item's index is a list of `(ID, position)` pairs for all the sequences in `seqs` containing the item.

``` python
data = [s.split() for s in [
    "a b c d e",
    "b b b d e",
    "c b c c a",
    "b b b c c"
]]

invertedindex(data)
# {'a': [(0, 0), (2, 4)],
#  'b': [(0, 1), (1, 0), (2, 1), (3, 0)],
#  'c': [(0, 2), (2, 0), (3, 3)],
#  'd': [(0, 3), (1, 3)],
#  'e': [(0, 4), (1, 4)]}
```

- `nextentries(data, entries)` scans the sequences in `data` from left to right after current entries `entries`, and returns each item and its respective following entries.

    - Each entry is a pair of `(ID, Position)` denoting the sequence ID and its respective matching position.

``` python
# same data from previous example

# the first positions of `c` among sequences.
entries = [(0, 2), (2, 0), (3, 3)]

nextentries(data, entries)
# {'d': [(0, 3)],
#  'e': [(0, 4)],
#  'b': [(2, 1)],
#  'c': [(2, 2), (3, 4)],
#  'a': [(2, 4)]}
```

Tools for flatten/unflatten a dictionary.

- `flatten(d, force=False)` flattens a dictionary by returning `(Path, Value`) tuples with each path `Path` from root to each value `Value`.

    - For each path, if any array with nested dictionary is encountered, the index of the array also becomes part of the path.

    - In default, only an array with nested dictionary is flatten. Instead, parameter `force` can be specified to flatten any array. Note that an empty array contains no child and disappears after being flatten.

``` python
flatten(json.loads("""{
  "name": "John",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}"""))
# {'name': 'John',
#  ('address', 'streetAddress'): '21 2nd Street',
#  ('address', 'city'): 'New York',
#  (('phoneNumbers', 0), 'type'): 'home',
#  (('phoneNumbers', 0), 'number'): '212 555-1234',
#  (('phoneNumbers', 1), 'type'): 'office',
#  (('phoneNumbers', 1), 'number'): '646 555-4567',
#  'children': [],
#  'spouse': None}
```

<a name="jsontools"></a>
### [`jsontools`](https://github.com/chuanconggao/extratools/blob/master/extratools/jsontools.py)

Tools for flatten/unflatten a JSON object.

- `flatten(data, force=False)` flattens a JSON object by returning `(Path, Value`) tuples with each path `Path` from root to each value `Value`.

    - For each path, if any array with nested dictionary is encountered, the index of the array also becomes part of the path.

    - In default, only an array with nested dictionary is flatten. Instead, parameter `force` can be specified to flatten any array. Note that an empty array contains no child and disappears after being flatten.

``` python
flatten(json.loads("""{
  "name": "John",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}"""))
# {'name': 'John',
#  'address.streetAddress': '21 2nd Street',
#  'address.city': 'New York',
#  'phoneNumbers[0].type': 'home',
#  'phoneNumbers[0].number': '212 555-1234',
#  'phoneNumbers[1].type': 'office',
#  'phoneNumbers[1].number': '646 555-4567',
#  'children': [],
#  'spouse': None}
```

<a name="settools"></a>
### [`settools`](https://github.com/chuanconggao/extratools/blob/master/extratools/settools.py)

Tools for set operations.

- `addtoset(s, x)` checks whether adding `x` to set `s` is successful.

Tools for set similarities.

- `jaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`.

- `multisetjaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two multi-sets (Counters) `a` and `b`.

- `weightedjaccard(a, b, key=sum)` computes the weighted [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`, using function `key` to compute the total weight of the elements within a set.

<a name="tabletools"></a>
### [`tabletools`](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

Tools for tables.

- `transpose(data)` returns the transpose of table `data`, i.e., switch rows and columns.

    - Useful to switch table `data` from row-based to column-based and backwards.

``` python
list(transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

- `loadcsv(path, delimiter=',')` loads a CSV file, from either a file path or a file object.

- `dumpcsv(path, data, delimiter=',')` dumps a table `data` in CSV, to either a file path or a file object.

<a name="mathtools"></a>
### [`mathtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/mathtools.py)

Tools for math.

- `safediv(a, b)` avoids the `division by zero` exception, by returning infinite with proper sign.

    - Closely referring [IEEE Standard 754](https://en.wikipedia.org/wiki/IEEE_754).

<a name="stattools"></a>
### [`stattools`](https://github.com/chuanconggao/extratools/blob/master/extratools/stattools.py)

Tools for statistics.

- `medianabsdev(data)` computes the [median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation) of a list of floats.

- `entropy(data)` computes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of a list of any items.

    - You can also pass a dictionary of `(item, frequency)` as frequency distribution to `data`.

- `histogram` is alias of a tool in `rangetools`.

Tools for binary classification.

- `teststats(truths, predictions)` matches the truth labels and the prediction labels. Return a tuples of `(tp, fp, tn, fn)` as [true positive, false positive, true negative, and false negative](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers).

- `accuracy(tp, fp, tn, fn)` returns the [accuracy](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers).

    - Note that you can simply call `accuracy(*teststats(truths, predictions))`.

- `precision(tp, fp, tn, fn)` and `recall(tp, fp, tn, fn)` return the [precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall).

- `f1(tp, fp, tn, fn, beta=1)` returns the [F-1 measure](https://en.wikipedia.org/wiki/F1_score) in default, and returns the F-β measure when `beta` is specified.

<a name="misctools"></a>
### [`misctools`](https://github.com/chuanconggao/extratools/blob/master/extratools/misctools.py)

Tools for miscellaneous purposes.

- `cmp(a, b)` restores the useful `cmp` function previously in Python 2.

    - Implemented according to [What's New in Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons).

- `parsebool(s)` parses a string to boolean, if its lowercase equals to either `1`, `true`, or `yes`.

<a name="printtools"></a>
### [`printtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/printtools.py)

Tools for non-functional but useful printing purposes.

- `print2(*args, **kwargs)` redirects the output of `print` to standard error.

    - The same parameters are accepted.

<a name="debugtools"></a>
### [`debugtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/debugtools.py)

Tools for non-functional but useful debugging purposes.

- `stopwatch()` returns both the duration since program start and the duration since last call in seconds.

    - Technically, the stopwatch starts when `debugtools` is imported.

- `peakmem()` returns the peak memory usage since program start.

    - In bytes on macOS, and in kilobytes on Linux.

## Data Structures

<a name="disjointsets"></a>
### [`disjointsets`](https://github.com/chuanconggao/extratools/blob/master/extratools/disjointsets.py)

[Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) with path compression, based a lot on this [implementation](https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py). After `d = DisjointSets()`:

- `d.add(x)` adds a new disjoint set containing `x`.

- `d[x]` returns the representing element of the disjoint set containing `x`.

- `d.disjoints()` returns all the representing elements and their respective disjoint sets.

- `d.union(*xs)` union all the elements in `xs` into a single disjoint set.

<a name="defaultlist"></a>
### [`defaultlist`](https://github.com/chuanconggao/extratools/blob/master/extratools/defaultlist.py)

A sub-class of `list` that automatically grows when setting an index beyond the list size.

- When creating a list, use `DefaultList(default, ...)` to specify a function that returns default value when visiting an unassigned index.

- This library is designed to be highly similar to `collections.defaultdict` in standard library.

``` python
l = DefaultList(lambda: None, range(10))

l[11] = 11

l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11]
```
