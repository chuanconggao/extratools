## Sequence Matching with Gap

Tools for matching sequences (including strings), with gaps allowed between matching items.

### `bestsubseqwithgap(a, key)`

Finds the best sub-sequence of `a` that maximizes the key function `key`, where gaps are allowed.

!!! warning
    This function reads the sequence at once.

``` python
bestsubseqwithgap([1, -2, 3, -4, 5, -6], sum)
# [1, 3, 5]
```

### `findallsubseqswithgap(a, b, overlap=False)`

Returns all the positions where `a` is a sub-sequence of `b`.

- In default, no overlapping is allowed. You can change this behavior by specify `overlap`.

- Unlike other function in `seqtools`, empty list is returned when `a` is empty.

!!! warning
    This function reads all sequences at once.

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
))
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

!!! warning
    This function reads all sequences at once.

``` python
list(commonsubseqwithgap(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1]
))
# [0, 1, 1, 1]
```

## Sub-Sequence Enumeration with Gap

Tools for enumerating sub-sequences with gap.

### `enumeratesubseqswithgap(seq)`

Enumerates all of `seq`'s non-empty sub-sequences in [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order).

- Although `seq` is a sub-sequence of itself, it is not returned.

!!! warning
    This function reads the sequence at once.

``` python
list(enumeratesubseqswithgap([0, 1, 0, 2]))
# [(0,),
#  (1,),
#  (0,),
#  (2,),
#  (0, 1),
#  (0, 0),
#  (0, 2),
#  (1, 0),
#  (1, 2),
#  (0, 2),
#  (0, 1, 0),
#  (0, 1, 2),
#  (0, 0, 2),
#  (1, 0, 2)]
```

