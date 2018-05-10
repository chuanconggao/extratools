[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

Tools for matching sequences (including strings), without gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

- `bestsubseq(a, key)` finds the best sub-sequence of `a` that maximizes the key function `key`.

``` python
bestsubseq([1, -2, 3, -4, 5, -6], sum)
# [5]
```

- `findallsubseqs(a, b, overlap=False)` returns all the positions where `a` is a sub-sequence of `b`.

    - In default, no overlapping is allowed. You can change the behavior by specify `overlap`.

    - Unlike other function in `seqtools`, nothing is returned when `a` is empty.

- `findsubseq(a, b)` returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

- `issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

- `commonsubseq(a, b)` finds the [longest common sub-sequence](https://en.wikipedia.org/wiki/Longest_common_substring_problem) among two sequences `a` and `b`.

``` python
commonsubseq(
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1]
)
# [0, 1, 1]
```

Tools for matching sequences (including strings), with gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

- `bestsubseqwithgap(a, key)` finds the best sub-sequence of `a` that maximizes the key function `key`, where gaps are allowed.

``` python
bestsubseqwithgap([1, -2, 3, -4, 5, -6], sum)
# [1, 3, 5]
```

- `findsubseqwithgap(a, b)` returns the matching positions where `a` is a sub-sequence of `b`, where gaps are allowed, or `None` when not found.

- `issubseqwithgap(a, b)` checks if `a` is a sub-sequence of `b`, where gaps are allowed.

- `commonsubseqwithgap(a, b)` finds the [longest common sub-sequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) among two sequences `a` and `b`, where gaps are allowed.

``` python
commonsubseqwithgap(
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1]
)
# [0, 1, 1, 1]
```

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

