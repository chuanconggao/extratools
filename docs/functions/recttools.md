[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/recttools.py)

!!! warning
    For tools specific to grid operations, please go to specific [documentation](recttools/grid).

!!! info
    Each point is defined as a tuple of its `(x, y)` positions in float.

    Each rectangle is defined as a tuple of its bottom left point and its top right point.

!!! danger
    Each rectangle is assumed to be valid, i.e., its bottom left point is at the bottom left of its top right point.

## Rectangle Basics

Tools for basic rectangle usages.

### `pointcmp`

`pointcmp(a, b)` compares the positions of points `a` and `b`, and returns:

- `1` if `b` is at the top right of `a`.

- `-1` if `b` is at the bottom left of `a`.

- `-2` if `b` is at the top left of `a`.

- `2` if `b` is at the bottom right of `a`.

- `0` if `a` and `b` are equal.

![`pointcmp`](recttools/pointcmp.svg)

!!! tip
    The behavior here is designed to be similar to [`cmp`](misctools#cmp).

``` python
pointcmp((1, 1), (2, 2))
# <PointCmp.TOP_RIGHT: 1>

pointcmp((1, 1), (2, 0))
# <PointCmp.BOTTOM_RIGHT: 2>

pointcmp((1, 1), (0, 0))
# <PointCmp.BOTTOM_LEFT: -1>

pointcmp((1, 1), (0, 2))
# <PointCmp.TOP_LEFT: -2>
```

### `allpoints`

`allpoints(rect)` returns all four points of the rectangle `rect`, in the order of counter-clockwise, starting from the bottom left point.

``` python
allpoints(((1, 1), (2, 3)))
# ((1, 1), (2, 1), (2, 3), (1, 3))
```

### `size`

`size(rect)` computes the size of the rectangle `rect`.

### `issubrect`

`issubrect(rect1, rect2)` checks if rectangle `rect1` is covered by another rectangle `rect2`.

![`issubrect`](recttools/issubrect.svg)

``` python
issubrect(
    ((1, 1), (3, 3)),
    ((0, 2), (4, 4))
)
# False

issubrect(
    ((1, 2), (3, 3)),
    ((0, 2), (4, 4))
)
# True
```

### `intersect`

`intersect(rect1, rect2)` computes the intersect of two rectangles `rect1` and `rect2`, or returns `None` if not intersected.

![`intersect`](recttools/intersect.svg)

``` python
intersect(
    ((1, 1), (3, 3)),
    ((0, 2), (4, 4))
)
# ((1, 2), (3, 3))

intersect(
    ((1, 1), (3, 3)),
    ((2, 4), (5, 6))
)
# None
```

### `union`

`union(rect1, rect2, force=False)` computes the union of two rectangles `rect1` and `rect2`, or returns `None` if not intersected.

- The union of two not intersected rectangles can be computed by specifying `force=True`.

![`union`](recttools/union.svg)

``` python
union(
    ((1, 1), (3, 3)),
    ((0, 2), (4, 4))
)
# ((0, 1), (4, 4))
```

![`union` when `force=True`](recttools/union_force.svg)

``` python
union(
    ((1, 1), (3, 3)),
    ((2, 4), (5, 6))
)
# None

union(
    ((1, 1), (3, 3)),
    ((2, 4), (5, 6)),
    force=True
)
# ((1, 1), (5, 6))
```

