[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

## Sequence Matching

Tools for matching sequences (including strings), without gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

### `bestsubseq(a, key)`

Finds the best sub-sequence of `a` that maximizes the key function `key`.

``` python
bestsubseq([1, -2, 3, -4, 5, -6], sum)
# [5]
```

### `findallsubseqs(a, b, overlap=False)`

Returns all the positions where `a` is a sub-sequence of `b`.

- In default, no overlapping is allowed. You can change this behavior by specify `overlap`.

- Unlike other function in `seqtools`, empty list is returned when `a` is empty.

``` python
list(findallsubseqs(
    [   0, 1, 0],
    [0, 0, 1, 0, 1, 0]
))
# [1]

list(findallsubseqs(
    [   0, 1, 0],
  # [         0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    overlap=True
))
# [1, 3]
```

### `findsubseq(a, b)`

Returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

``` python
findsubseq(
    [   0, 1, 0],
    [0, 0, 1, 0, 1, 0]
)
# 1
```

### `issubseq(a, b)`

Checks if `a` is a sub-sequence of `b`.

``` python
issubseq(
    [   0, 1, 0],
    [0, 0, 1, 0, 1, 0]
)
# True
```

### `commonsubseq(a, b)`

Finds the [longest common sub-sequence](https://en.wikipedia.org/wiki/Longest_common_substring_problem) among two sequences `a` and `b`.

``` python
commonsubseq(
    [   0, 1, 1,   0, 1],
    [0, 0, 1, 1, 1]
)
# [0, 1, 1]
```

## Sequence Matching with Gap

Tools for matching sequences (including strings), with gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

### `bestsubseqwithgap(a, key)`

Finds the best sub-sequence of `a` that maximizes the key function `key`, where gaps are allowed.

``` python
bestsubseqwithgap([1, -2, 3, -4, 5, -6], sum)
# [1, 3, 5]
```

### `findallsubseqswithgap(a, b, overlap=False)`

Returns all the positions where `a` is a sub-sequence of `b`.

- In default, no overlapping is allowed. You can change this behavior by specify `overlap`.

- Unlike other function in `seqtools`, empty list is returned when `a` is empty.

``` python
list(findallsubseqswithgap(
    [0,    1,    1],
  # [   0,             1, 1],
    [0, 0, 1, 0, 1, 0, 1, 1]
))
# [[0, 2, 4], [1, 6, 7]]

# Enumerates all the possible matchings.
list(findallsubseqswithgap(
   [0,    1,    1],
 # [0,    1,          1],
 # ...
 # [               0, 1, 1],
   [0, 0, 1, 0, 1, 0, 1, 1],
   overlap=True
)
# [[0, 2, 4],
#  [0, 2, 6],
#  [0, 2, 7],
#  [0, 4, 6],
#  [0, 4, 7],
#  [0, 6, 7],
#  [1, 2, 4],
#  [1, 2, 6],
#  [1, 2, 7],
#  [1, 4, 6],
#  [1, 4, 7],
#  [1, 6, 7],
#  [3, 4, 6],
#  [3, 4, 7],
#  [3, 6, 7],
#  [5, 6, 7]]
```

### `findsubseqwithgap(a, b)`

Returns the matching positions where `a` is a sub-sequence of `b`, where gaps are allowed, or `None` when not found.

``` python
list(findsubseqwithgap(
    [0,    1,    1],
    [0, 0, 1, 0, 1, 0]
))
# [0, 2, 4]
```

### `issubseqwithgap(a, b)`

Checks if `a` is a sub-sequence of `b`, where gaps are allowed.

``` python
list(issubseqwithgap(
    [0,    1,    1],
    [0, 0, 1, 0, 1, 0]
))
# True
```

### `commonsubseqwithgap(a, b)`

Finds the [longest common sub-sequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) among two sequences `a` and `b`, where gaps are allowed.

``` python
commonsubseqwithgap(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1]
)
# [0, 1, 1, 1]
```

## Sequence Alignment and Join

Tools for aligning and joining sequences.

### `align(a, b, cost=None, bound=inf, default=None)`

[Aligns](https://en.wikipedia.org/wiki/Sequence_alignment) two sequences `a` and `b`, such that the total cost of the aligned sequences given the pair-wise cost function `cost(x, y)` is minimized.

- Assume the sequences after alignment are `a'` and `b'`. The total cost is `sum(cost(x, y) for x, y in zip(a', b'))`.

- Both the minimum total cost and the respective aligned sequences are returned as a tuple.

- In default, the cost function `cost(x, y)` returns `0` when `x == y` and `1` when not. This is equal to the [edit distance](https://en.wikipedia.org/wiki/Edit_distance).

- To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

- If there are multiple alignments having the same cost, the leftmost one is returned.

``` python
align(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1]
)
# (2, ([0, None, 1, 1,    0, 1],
#      [0,    0, 1, 1, None, 1]))

align(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1],
    bound=1
)
# None
```

### `match(a, b, default=None)`

Matches two sequences `a` and `b` in pairs, such that the total number of matching pairs is maximized.

- If there are multiple alignments having the same number, the leftmost one is returned.

``` python
list(match(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1]
))
# [(0, 0),
#  (None, 0),
#  (1, 1),
#  (1, 1),
#  (0, None),
#  (1, 1)]
```

### `join(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)`

Joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

- If both two sequences are sorted according to `leftkey` and `rightkey`, respectively, then optimized `sortedtools.join` with the same API should be used for better efficiency.

- Unlike `sortedtools.join`, `join` is just a wrapper of `toolz.itertools.join` with a slightly more friendly API.

``` python
list(join(
    [   -1, -1, -2,    -4, -5,    -6],
    [0,  1,  1,  2, 3,  4,  5, 5],
    leftkey=abs, leftdefault=None
))
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

## Sequence Comparison

Tools for comparing sequences (including strings).

### `productcmp(x, y)`

Compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

- Throw exception if `x` and `y` have different lengths.

``` python
productcmp([1, 2, 3], [4, 5, 6])
# 1

productcmp([1, 2, 3], [4, 3, 2])
# None
```

## Sequence Sorting

Tools for sorting sequences.

### `sortedbyrank(data, ranks, reverse=False)`

Returns the sorted list of `data`, according to the respective rank of each individual element in `ranks`.

``` python
sortedbyrank(['a', 'b', 'c'], [3, 2, 1])
# ['c', 'b', 'a']
```

## Sequence Encoding/Decoding

Tools for encoding/decoding sequences.

### `compress(data, key=None)`

Compresses the sequence by encoding continuous identical `Item` to `(Item, Count)`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

- Different from [`itertools.compress`](https://docs.python.org/3.6/library/itertools.html#itertools.compress).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

### `decompress(data)`

Decompresses the sequence by decoding `(Item, Count)` to continuous identical `Item`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

``` python
list(decompress([(1, 1), (2, 2), (3, 3), (4, 4)]))
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

### `todeltas(data, op=operator.sub)`

Compresses the sequence by encoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

- For custom type of item, either define the `-` operator or specify the `op` function computing the difference.

``` python
list(todeltas([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
```

### `fromdeltas(data, op=operator.add)`

Decompresses the sequence by decoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

- For custom type of item, either define the `+` operator or specify the `op` function merging the difference.

``` python
list(fromdeltas([1, 1, 0, 1, 0, 0, 1, 0, 0, 0]))
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

