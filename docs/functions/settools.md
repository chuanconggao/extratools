[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/settools.py)

!!! info
    A set is a subset/superset of itself.

!!! warning
    For tools related to specific tasks, please go to the respective documentation:

    - [Set similarity](set similarity).

## Set Basics

Tools for basic set usages.

### `addtoset`

`addtoset(s, x)` checks whether adding `x` to set `s` is successful.

``` python
s = set()

addtoset(s, 1)
# True

addtoset(s, 1)
# False
```

## Set Filtering

Tools for filtering set or a sequence of sets.

### `dropsubsetsof` and `dropsupersetsof`

`dropsubsetsof(a, b)`/`dropsupersetsof(a, b)` drops any set in `a` that is a subset/superset of another set `b`.

``` python
list(dropsubsetsof(
    [{1,}, {1, 2}, {1, 2, 3}, {2, 3}],
    {2, 3, 4}
))
# [{1}, {1, 2}, {1, 2, 3}]

list(dropsupersetsof(
    [{1,}, {1, 2}, {1, 2, 3}, {2, 3}],
    {2}
))
# [{1}]
```

### `dropsubsets` and `dropsupersets`

`dropsubsets(a)`/`dropsupersets(a)` drops any set in `a` that is a subset/superset of another set in `a`.

``` python
list(dropsubsets([
    {1,}, {1, 2}, {1, 2, 3}, {2, 3}, {2, 3, 4}
]))
# [{1, 2, 3}, {2, 3, 4}]

list(dropsupersets([
    {1,}, {1, 2}, {1, 2, 3}, {2, 3}, {2, 3, 4}
]))
# [{1}, {2, 3}]
```

## Set Matching

Tools for matching sets.

### `bestsubset`

`bestsubset(a, key)` finds the best sub-set of `a` that maximizes the key function `key`.

``` python
bestsubset({1, -2, 3, -4, 5, -6}, sum)
#          {1,     3,     5}
```

### `setcover`

`setcover(whole, covered, key=len)` solves the [set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem) by covering the universe set `whole` as best as possible, using a subset of the covering sets `covered`.

- In default, the size of each set `len` is used as key function `key` to measure the coverage.

!!! warning
    This is an approximate algorithm, which means the returned result is not always the best.

``` python
list(setcover(
    { 1, 2, 3,         4,         5},
    [{1, 2, 3}, {2, 3, 4}, {2, 4, 5}]
))
# [frozenset({1, 2, 3}), frozenset({2, 4, 5})]
```
