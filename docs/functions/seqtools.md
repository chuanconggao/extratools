[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

!!! warning
    For tools specific to sequence without gap, please go to specific [documentation](seqtools/seqwithoutgap).

    For tools specific to sequence with gap, please go to specific [documentation](seqtools/seqwithgap).

!!! success
    If not explicitly noted, a sequence refers to not only list, tuple, string, or [array](https://docs.python.org/3/library/array.html), but any iterable.

    If not explicitly noted, a function is lazy, where each sequence is processed incrmentally only when necessary and returned incrmentally as a generator.

!!! info
    Empty sequence is always a sub-sequence of any other sequence.

    A sequence is always a sub-sequence of itself.

## Sequence Matching

### `matchingfrequencies`

`matchingfrequencies(*seqs, key=None)` returns each item and the respective number of sequences in `seqs` contains it.

- Optional key function `key` can be specified.

!!! tip
    If each sequence is sorted, then optimized [`sortedtools.matchingfrequencies`](sortedtools#matchingfrequencies) with the same API should be used for better efficiency.

    For the frequency of each item within a single sequence, use [`toolz.itertoolz.frequencies`](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.frequencies).

``` python
list(matchingfrequencies(
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2]
))
# [(0, 2), (1, 4), (2, 3), (3, 2), (4, 2)]
```

## Sequence Alignment and Join

Tools for aligning and joining sequences.

### `match`

`match(a, b, default=None)` matches two sequences `a` and `b` in pairs, such that the total number of matching pairs is maximized.

- If there are multiple alignments having the same number, the leftmost one is returned.

!!! warning
    This function reads all sequences at once.

!!! tip
    If both two sequences are sorted, respectively, then optimized [`sortedtools.sortedmatch`](sortedtools#sortedmatch) with the same API should be used for better efficiency.

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

### `align`

`align(a, b, cost=None, bound=inf, default=None)` computes the [alignment](https://en.wikipedia.org/wiki/Sequence_alignment) two sequences `a` and `b`, such that the total cost of the aligned sequences given the pair-wise cost function `cost(x, y)` is minimized.

- Assume the sequences after alignment are `a'` and `b'`. The total cost is `sum(cost(x, y) for x, y in zip(a', b'))`.

- Both the minimum total cost and the respective aligned sequences are returned as a tuple.

- In default, the cost function `cost(x, y)` returns `0` when `x == y` and `1` when not. This is equal to the [edit distance](https://en.wikipedia.org/wiki/Edit_distance).

- To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

- If there are multiple alignments having the same cost, the leftmost one is returned.

!!! warning
    This function reads all sequences at once.

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

### `join`

`join(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)` joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

!!! warning
    This function reads the first sequence at once.

!!! tip
    If both two sequences are sorted according to `leftkey` and `rightkey`, respectively, then optimized [`sortedtools.sortedjoin`](sortedtools#sortedjoin) with the same API should be used for better efficiency.

!!! info
    `join` is just a wrapper of [`toolz.itertools.join`](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.join) with the same more friendly API of [`sortedtools.sortedjoin`](sortedtools#sortedjoin).

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

### `templateseq`

`templateseq(seqs, default=None, simple=True)` finds the common template of all the sequences `seqs`. `default=None` is used to denote any placeholder sub-sequence.

- For better performance, option `simple` is enabled in default for only one scan of the sequences. However, it may work incorrectly for more complex template, which is:

    - Any part of the template appears more than once in the same sequence,
    
    - Any part of the template does not always appear before or after than another according to the same order part among sequences.

!!! warning
    This function reads all the sequences at once.

    This function reads all the sequences more than once when `simple = False`.

!!! tip
    Essentially, each template is a closed sequential pattern covering all the sequences. Please check [PrefixSpan-Py](https://github.com/chuanconggao/PrefixSpan-py) for more advanced scenarios.

``` python
list(templateseq((
    s.split() for s in [
        "Alice likes tea and coffee !",
        "Bob likes sushi and ramen !",
        "Elisa or Anna likes icecream and cake and cookie !"
    ]
), default='*'))
# ['*', 'likes', '*', 'and', '*', '!']

list(templateseq((
    s.split() for s in [
        "Alice likes tea and coffee !",
        "Bob likes sushi and ramen !",
        "Elisa or Anna likes icecream and cake and cookie !"
    ]
), default='*', simple=False))
# ['*', 'likes', '*', 'and', '*', '!']

# For more complex data.
list(templateseq((
    s.split() for s in [
        "! Alice likes tea and coffee ! !",
        "Bob likes sushi and ramen ! !",
        "Elisa or Anna likes icecream and cake and cookie ! !"
    ]
), default='*'))
# Incorrect template.
# ['*', 'likes', '*', 'and', '*']

list(templateseq((
    s.split() for s in [
        "! Alice likes tea and coffee ! !",
        "Bob likes sushi and ramen ! !",
        "Elisa or Anna likes icecream and cake and cookie ! !"
    ]
), default='*', simple=False))
# ['*', 'likes', '*', 'and', '*', '!', '!']
```

## Sequence Comparison

Tools for comparing sequences.

### `productcmp`

`productcmp(x, y)` compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

- Throw exception if `x` and `y` have different lengths.

``` python
productcmp(
    [1, 2, 3],
    [4, 5, 6]
)
# 1

productcmp(
    [1, 2, 3],
    [4, 3, 2]
)
# None
```

## Sequence Sorting

Tools for sorting sequences.

### `sortedbyrank`

`sortedbyrank(data, ranks, reverse=False)` returns the sorted list of `data`, according to the respective rank of each individual element in `ranks`.

``` python
sortedbyrank(
    ['a', 'b', 'c'],
    [  3,   2,   1]
)
# ['c', 'b', 'a']
```

## Sequence Encoding/Decoding

Tools for encoding/decoding sequences.

### `compress`

`compress(data, key=None)` compresses the sequence by encoding continuous identical `Item` to `(Item, Count)`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

!!! warning
    Different from [`itertools.compress`](https://docs.python.org/3.6/library/itertools.html#itertools.compress).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

### `decompress`

`decompress(data)` decompresses the sequence by decoding `(Item, Count)` to continuous identical `Item`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

``` python
list(decompress([(1, 1), (2, 2), (3, 3), (4, 4)]))
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

### `todeltas`

`todeltas(data, op=operator.sub)` compresses the sequence by encoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

- For custom type of item, either define the `-` operator or specify the `op` function computing the difference.

``` python
list(todeltas([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
```

### `fromdeltas`

`fromdeltas(data, op=operator.add)` decompresses the sequence by decoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

- For custom type of item, either define the `+` operator or specify the `op` function merging the difference.

``` python
list(fromdeltas([1, 1, 0, 1, 0, 0, 1, 0, 0, 0]))
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

## Sequence Transformation

Tools for transforming sequences.

### `iter2seq`

`iter2seq(iterable, target=tuple)` converts any iterable sequence `iterable` to an indexable and sizable sequence with type `target=tuple` if necessary, defaults to tuple.

!!! warning
    This function reads the sequence at once.

!!! tip
    Useful if you need to scan the sequence more than once.

### `seq2grams`

`seq2grams(seq, n, pad=no_default)` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of sequence `seq`.

- Optional padding at the start and end can be added by specifying `pad`.

``` python
list(seq2grams(range(5), 3))
# [(0, 1, 2),
#  (1, 2, 3),
#  (2, 3, 4)]

list(seq2grams(range(5), 3, pad=None))
# [(None, None, 0),
#  (None, 0, 1),
#  (0, 1, 2),
#  (1, 2, 3),
#  (2, 3, 4),
#  (3, 4, None),
#  (4, None, None)]
```
