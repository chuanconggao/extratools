[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/recttools.py)

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

## Grid Operations

Tools for operating on grid.

### `grid`

`grid(rect, rows, cols)` divides the rectangle `rect` into `rows` rows and `cols` columns, in the order of left to right and bottom to top.

- The returning order of each sub-rectangle is considered its ID. It is utilized by [`locatebyid`](#locatebyid), [`locatebypos`](#locatebypos), [`locatebypoint`](#locatebypoint), and [`heatmap`](#heatmap).

![`grid`](recttools/grid.svg)

``` python
list(grid(
    ((1, 1), (3, 4)),
    3, 4
))
# [((1.0, 1.0), (1.5, 2.0)),
#  ((1.5, 1.0), (2.0, 2.0)),
#  ((2.0, 1.0), (2.5, 2.0)),
#  ((2.5, 1.0), (3.0, 2.0)),
#  ((1.0, 2.0), (1.5, 3.0)),
#  ((1.5, 2.0), (2.0, 3.0)),
#  ((2.0, 2.0), (2.5, 3.0)),
#  ((2.5, 2.0), (3.0, 3.0)),
#  ((1.0, 3.0), (1.5, 4.0)),
#  ((1.5, 3.0), (2.0, 4.0)),
#  ((2.0, 3.0), (2.5, 4.0)),
#  ((2.5, 3.0), (3.0, 4.0))]
```

### `locatebyid`

`locatebyid(rect, rows, cols, rectid)` finds the sub-rectangle and its ID within rectangle `rect` by a grid of `rows` rows and `cols` columns, according to its ID defined in [`grid`](#grid).

!!! tip
    The ID is also returned to ensure the same returning type of [`locatebypos`](#locatebypos) and [`locatebypoint`](#locatebypoint).

![`locatebypos`](recttools/locatebypos.svg)

``` python
locatebyid(
    ((1, 1), (3, 4)),
    3, 4,
    9
)
# (9, ((1.5, 3.0), (2.0, 4.0)))
```

### `locatebypos`

`locatebypos(rect, rows, cols, pos)` finds the sub-rectangle and its ID within rectangle `rect` by a grid of `rows` rows and `cols` columns, according to the position of `(row, col)`.

![`locatebypos`](recttools/locatebypos.svg)

``` python
locatebypos(
    ((1, 1), (3, 4)),
    3, 4,
    (2, 1)
)
# (9, ((1.5, 3.0), (2.0, 4.0)))
```

### `locatebypoint`

`locatebypoint(rect, rows, cols, point)` finds the sub-rectangle and its ID within rectangle `rect` by a grid of `rows` rows and `cols` columns.

![`locatebypoint`](recttools/locatebypoint.svg)

``` python
locatebypoint(
    ((1, 1), (3, 4)),
    3, 4,
    (2.75, 2.75)
)
# (7, ((2.5, 2.0), (3.0, 3.0)))
```

### `heatmap`

`heatmap(rect, rows, cols, points)` computes the heatmap within rectangle `rect` by a grid of `rows` rows and `cols` columns.

![`heatmap`](recttools/heatmap.svg)

``` python
heatmap(
    ((1, 1), (3, 4)),
    3, 4,
    [(1.5, 1.25), (1.5, 1.75), (2.75, 2.75), (2.75, 3.5)]
)
# {1: 2, 7: 1, 11: 1}
```
