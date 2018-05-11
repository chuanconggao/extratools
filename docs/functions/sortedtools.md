[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

## Sequence Matching

Tools for matching sorted sequences.

### `sortedcommon(a, b, key=None)`

Returns the common elements between `a` and `b`.

- When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) & set(b))` but more efficient.

### `sortedalone(a, b, key=None)`

Returns the elements not in both `a` and `b`.

- When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted((set(a) | set(b)) - (set(a) & set(b)))` but more efficient.

### `sorteddiff(a, b, key=None)`

Returns the elements only in `a` and not in `b`.

- When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) - set(b))` but more efficient.

### `issubsorted(a, b, key=None)`

Checks if `a` is a sorted sub-sequence of `b`.

- When both `a` and `b` are sorted sets with no duplicate element, equal to `set(a) <= set(b)` but more efficient.

## Sequence Join

Tools for joining sorted sequences.

### `sortedjoin(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)`

Joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

- Two sequences must be already sorted according to `leftkey` and `rightkey`, respectively.

- `sortedjoin` is completely lazy, and more efficient than `seqtools.join` and its underneath `toolz.itertools.join`.

``` python
list(sortedjoin(
    [-1, -1, -2, -4, -5, -6],
    [0, 1, 1, 2, 3, 4, 5, 5],
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
