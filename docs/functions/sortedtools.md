[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

!!! info
    As each sorted sequence is a sequence, tools in `seqtools` can also be applied here. `sortedtools` only contains tools that either are unique to the concept of sorted sequence or have more efficient implementations.

!!! danger
    For most tools here except `issorted`, each sequence must already be sorted.

## Sequence Check

### `issorted(seq, key=None)`

Returns if sequence `seq` is already sorted, optionally according to the key function `key`.

``` python
issorted([1, 2, 2, 3])
# True
```

## Sequence Matching

Tools for matching sorted sequences.

### `sortedcommon(a, b, key=None)`

Returns the common elements between `a` and `b`, optionally according to the key function `key`.

!!! info
    When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) & set(b))` but more efficient.

``` python
list(sortedcommon(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [2, 3]
```

### `sortedalone(a, b, key=None)`

Returns the elements not in both `a` and `b`, optionally according to the key function `key`.

!!! info
    When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted((set(a) | set(b)) - (set(a) & set(b)))` but more efficient.

``` python
list(sortedalone(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [1, 2, 4, 4]
```

### `sorteddiff(a, b, key=None)`

Returns the elements only in `a` and not in `b`, optionally according to the key function `key`.

!!! info
    When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) - set(b))` but more efficient.

``` python
list(sorteddiff(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [1, 2]
```

### `issubsorted(a, b, key=None)`

Checks if `a` is a sorted sub-sequence of `b`, optionally according to the key function `key`.

- When both `a` and `b` are sorted sets with no duplicate element, equal to `set(a) <= set(b)` but more efficient.

``` python
issubsorted(
    [1, 2, 2, 3],
    [1, 2, 2, 3, 4, 4]
)
# True
```

### `matchingfrequencies(*seqs, key=None)`

Returns each item and the respective number of sequences in `seqs` contains it.

- Optional key function `key` can be specified.

!!! success
    This implementation is space efficient. If there are $n$ sequences, only $O(n)$ space is used.

!!! tip
    For the frequency of each item within a single sequence, use `toolz.itertoolz.frequencies`.

``` python
list(matchingfrequencies(
    [1, 2, 2, 3],
    [   2,    3,    4, 5],
    [1,       3, 3, 4]
))
# [(1, 2), (2, 2), (3, 3), (4, 2), (5, 1)]
```

## Sequence Alignment and Join

Tools for aligning and joining sorted sequences.

### `sortedmatch(a, b, default=None)`

Matches two sorted sequences `a` and `b` in pairs, such that the total number of matching pairs is maximized.

- If there are multiple alignments having the same number, the leftmost one is returned.

!!! success
    `sortedmatch` is lazy and more efficient than `seqtools.match`.

``` python
list(sortedmatch(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [(1, None),
#  (2, 2),
#  (2, None),
#  (3, 3),
#  (None, 4),
#  (None, 4)]
```

### `sortedjoin(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)`

Joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

- Two sequences must be already sorted according to `leftkey` and `rightkey`, respectively.

!!! success
    `sortedjoin` is lazy and more efficient than `seqtools.join` and its underneath `toolz.itertools.join`.

``` python
list(sortedjoin(
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
