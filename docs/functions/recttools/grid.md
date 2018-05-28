## Grid Operations

Tools for operating on grid.

### `grid`

`grid(rect, rows, cols)` divides the rectangle `rect` into `rows` rows and `cols` columns, in the order of left to right and bottom to top.

- The returning order of each sub-rectangle is considered its ID. It is utilized by [`locatebyid`](#locatebyid), [`locatebypos`](#locatebypos), [`locatebypoint`](#locatebypoint), and [`heatmap`](#heatmap).

!!! tip
    From the rectangle ID, you can easily get the position tuple `pos, col = divmod(rectid, cols)`.

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

- Return `None` when not in grid.

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

- Return `None` when not in grid.

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

- Return `None` when not in grid.

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

`heatmap(rect, rows, cols, points, usepos=False)` computes the heatmap within rectangle `rect` by a grid of `rows` rows and `cols` columns.

- Specify `usepos=True` to return the position of `(row, col)` instead of rectangle ID for each sub-rectangle.

![`heatmap`](recttools/heatmap.svg)

``` python
heatmap(
    ((1, 1), (3, 4)),
    3, 4,
    [(1.5, 1.25), (1.5, 1.75), (2.75, 2.75), (2.75, 3.5), (3.5, 2.5)]
)
# {1: 2, 7: 1, 11: 1, None: 1}

heatmap(
    ((1, 1), (3, 4)),
    3, 4,
    [(1.5, 1.25), (1.5, 1.75), (2.75, 2.75), (2.75, 3.5), (3.5, 2.5)],
    usepos=True
)
# {(0, 1): 2, (1, 3): 1, (2, 3): 1, None: 1}
```

