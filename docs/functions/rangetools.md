[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/rangetools.py)

!!! warning
    Each range is closed on the left side, and open on the right side.

## Range Statistics

Tools for statistics over ranges.

### `histogram`

`histogram(thresholds, data, leftmost=-inf)` computes the [histogram](https://en.wikipedia.org/wiki/Histogram) over all the floats in `data`.

- The search space is divided by the thresholds of bins specified in `thresholds`.

- Each bin of the histogram is labelled by its lower threshold.

    - All values in the bin are no less than the current threshold and less than the next threshold.

    - The first bin is labelled by `leftmost`, which is `-inf` in default.

!!! danger
    `thresholds` must be a sorted list.

``` python
histogram(
    [   0.1,                0.5,           0.8, 0.9],
    [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
)
# {-inf: 1, 0.1: 4, 0.5: 3, 0.8: 1, 0.9: 2}
```

## Range Querying

Tools for querying ranges.

### `rangequery`

`rangequery(keyvalues, query, func=min)` efficiently finds the best value from the covered values in `keyvalues`, if each key in `keyvalues` is within the query range `query`.

- `func` defines how the best value is computed, and defaults to `min` for minimum value.

!!! info
    Implemented by [SegmentTree](/datastructures/segmenttree.md) to solve the [range minimum query](https://en.wikipedia.org/wiki/Range_minimum_query) problem.

``` python
rangequery(
    {0.1: 1, 0.2: 3, 0.3: 0},
            (0.2,            0.4)
)
# 0
```

## Range Transformation

Tools for transformations over ranges.

### `intersect`

`intersect(a, b)` computes the overlapping of two ranges `a` and `b`. Returns `None` if there is no overlapping.

``` python
intersect((0, 0.6), (0.4, 1))
# (0.4, 0.6)
```

### `union`

`union(a, b)` computes the merging of two ranges `a` and `b`. Returns `None` if there is no overlapping.

``` python
union((0, 0.6), (0.4, 1))
# (0, 1)
```

### `rangecover`

`rangecover(whole, covered)` solves the variation of the [set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem) by covering the universe range `whole` as best as possible, using a subset of the covering ranges `covered`.

!!! warning
    This is an approximate algorithm, which means the returned result is not always the best.

``` python
list(rangecover(
     (0,                                                 1),
    [(0, 0.4), (0.2, 0.5), (0.5, 0.8), (0.6, 0.9), (0.8, 1)]
))
# [(0, 0.4), (0.5, 0.8), (0.8, 1), (0.2, 0.5)]
```

### `covers`

`covers(covered)` merges the covered ranges `covered` to resolve any overlap.

!!! danger
    Covered ranges in `covered` must be sorted by the left side of each range.

``` python
list(covers([(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)]))
# [(-inf, 0), (0.1, 0.2), (0.5, 0.9)]
```

### `gaps`

`gaps(covered, whole=(-inf, inf))` computes the uncovered ranges of the whole range `whole`, given the covered ranges `covered`.

!!! danger
    Covered ranges in `covered` must be sorted by the left side of each range.

!!! info
    Overlaps among covered ranges `covered` are resolved, like [`covers(covered)`](#covers).

``` python
list(gaps(
    [(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)],
           (0,                                     1)
))
# [(0, 0.1), (0.2, 0.5), (0.9, 1)]
```
