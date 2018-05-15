## Sequence Matching without Gap

Tools for matching sequences (including strings), without gaps allowed between matching items.

### `bestsubseq`

`bestsubseq(a, key)` finds the best sub-sequence of `a` that maximizes the key function `key`.

!!! warning
    This function reads the sequence at once.

``` python
bestsubseq([1, -2, 3, -4, 5, -6], sum)
# [5]
```

### `findallsubseqs`

`findallsubseqs(a, b, overlap=False)` returns all the positions where `a` is a sub-sequence of `b`.

- In default, no overlapping is allowed. You can change this behavior by specify `overlap`.

- Unlike other function in [`seqtools`](.), empty list is returned when `a` is empty.

!!! warning
    This function reads the first sequence at once.

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

### `findsubseq`

`findsubseq(a, b)` returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

!!! warning
    This function reads the first sequence at once.

``` python
findsubseq(
    [   0, 1, 0],
    [0, 0, 1, 0, 1, 0]
)
# 1
```

### `issubseq`

`issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

!!! warning
    This function reads the first sequence at once.

``` python
issubseq(
    [   0, 1, 0],
    [0, 0, 1, 0, 1, 0]
)
# True
```

### `commonsubseq`

`commonsubseq(a, b)` finds the [longest common sub-sequence](https://en.wikipedia.org/wiki/Longest_common_substring_problem) among two sequences `a` and `b`.

!!! warning
    This function reads all sequences at once.

``` python
list(commonsubseq(
    [   0, 1, 1,   0, 1],
    [0, 0, 1, 1, 1]
))
# [0, 1, 1]
```

## Sub-Sequence Enumeration without Gap

Tools for enumerating sub-sequences without gap.

### `enumeratesubseqs`

`enumeratesubseqs(seq)` enumerates all of `seq`'s non-empty sub-sequences in [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order).

- Although `seq` is a sub-sequence of itself, it is not returned.

!!! warning
    This function reads the sequence at once.

``` python
list(enumeratesubseqs([0, 1, 0, 2]))
# [[0],
#  [0, 1],
#  [0, 1, 0],
#  [1],
#  [1, 0],
#  [1, 0, 2],
#  [0],
#  [0, 2],
#  [2]]
```

### `nonsharingsubseqs`

`nonsharingsubseqs(*seqs, closed=True)` finds all the non-sharing non-empty sub-sequences among `seqs`, such that the item of each sub-sequence only appears in any sequence of `seqs` containing that respective sub-sequence.

- Each sub-sequence is a tuple of items.

- `closed=True` can be specified to return only the longest sub-sequences, i.e. no sub-sequence of is a sub-sequence of another sub-sequence.

!!! warning
    This function reads all sequences at once.

``` python
db = [
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2],
]

nonsharingsubseqs(db)
# {(0,): 2,
#  (1,): 4,
#  (2,): 3,
#  (3, 4): 2}

nonsharingsubseqs(db, closed=False)
# {(0,): 2,
#  (1,): 4,
#  (2,): 3,
#  (3,): 2,
#  (3, 4): 2,
#  (4,): 2}
```

## Sequence Partition

Tools for sequence partition.

### `partitionbysubseqs`

`partitionbysubseqs(subseqs, seq)` finds the partitions of sequence `seq`, according to a known sets of sub-sequences `subseqs`.

- For unknown sub-sequences, the longest ones are outputted.

!!! warning
    This function reads the sequence `seq` at once.

``` python
list(partitionbysubseqs(
    [
        (0,),
        (1,),
        (2,),
        (3, 4)
    ],
    [-1, 0, 1, 1, 5, 6, 3, 4, 7]
))
# [[-1], [0], [1], [1], [5, 6], [3, 4], [7]]
```
