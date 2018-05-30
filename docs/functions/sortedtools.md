[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

!!! danger
    For most tools here except [`issorted`](#issorted), each sequence must already be sorted.

!!! info
    Tools in [`seqtools`](seqtools) can also be applied here. `sortedtools` only contains tools that either are unique to the concept of sorted sequence or have more efficient implementations.

## Sequence Check

### `issorted`

`issorted(seq, key=None)` returns if sequence `seq` is already sorted, optionally according to the key function `key`.

``` python
issorted([1, 2, 2, 3])
# True
```

## Sequence Matching

Tools for matching sorted sequences.

### `issubsorted`

`issubsorted(a, b, key=None)` checks if `a` is a sorted sub-sequence of `b`, optionally according to the key function `key`.

- When both `a` and `b` are sorted sets with no duplicate element, equal to `set(a) <= set(b)` but more efficient.

``` python
issubsorted(
    [1, 2, 2, 3],
    [1, 2, 2, 3, 4, 4]
)
# True
```

### `sortedall`

`sortedall(a, b, key=None)` returns the elements in either `a` or `b`, optionally according to the key function `key`.

!!! success
    When both `a` and `b` are sorted [multisets](https://en.wikipedia.org/wiki/Multiset), equal to the union of `a` and `b` but more efficient.

``` python
list(sortedall(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [1, 2, 2, 3, 4, 4]
```

### `sortedcommon`

`sortedcommon(a, b, key=None)` returns the common elements between `a` and `b`, optionally according to the key function `key`.

!!! success
    When both `a` and `b` are sorted multisets, equal to the intersection of `a` and `b` but more efficient.

``` python
list(sortedcommon(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [2, 3]
```

### `sorteddiff`

`sorteddiff(a, b, key=None)` returns the elements only in `a` and not in `b`, optionally according to the key function `key`.

!!! success
    When both `a` and `b` are sorted multisets, equal to the [difference](https://en.wikipedia.org/wiki/Set_(mathematics)#Complements) between `a` and `b` but more efficient.

``` python
list(sorteddiff(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [1, 2]
```

### `sortedalone`

`sortedalone(a, b, key=None)` returns the elements not in both `a` and `b`, optionally according to the key function `key`.

!!! success
    When both `a` and `b` are sorted multisets, equal to the difference between the union of `a` and `b` and the intersection of `a` and `b` but more efficient.

``` python
list(sortedalone(
    [1, 2, 2, 3],
    [   2,    3, 4, 4]
))
# [1, 2, 4, 4]
```

## Sequence Alignment and Join

Tools for aligning and joining sorted sequences.

### `matchingfrequencies`

`matchingfrequencies(*seqs, key=None)` returns each item and the respective number of sequences in `seqs` contains it.

- Optional key function `key` can be specified.

!!! success
    This implementation is space efficient. If there are $n$ sequences, only $O(n)$ space is used.

    `sortedtools.matchingfrequencies` is more efficient than [`seqtools.matchingfrequencies`](seqtools#matchingfrequencies).

!!! tip
    For the frequency of each item within a single sequence, use [`toolz.itertoolz.frequencies`](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.frequencies).

``` python
list(matchingfrequencies(
    [1, 2, 2, 3],
    [   2,    3,    4, 5],
    [1,       3, 3, 4]
))
# [(1, 2), (2, 2), (3, 3), (4, 2), (5, 1)]
```

### `sortedmatch`

`sortedmatch(a, b, default=None)` matches two sorted sequences `a` and `b` in pairs, such that the total number of matching pairs is maximized.

- If there are multiple alignments having the same number, the leftmost one is returned.

!!! success
    `sortedmatch` is more efficient than [`seqtools.match`](seqtools#match).

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

### `sortedjoin`

`sortedjoin(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)` joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

- Two sequences must be already sorted according to `leftkey` and `rightkey`, respectively.

!!! success
    `sortedjoin` is more efficient than [`seqtools.join`](seqtools#join) and its underneath [`toolz.itertools.join`](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.join).

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
