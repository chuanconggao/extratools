[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

!!! info
    A table is a list of rows having the same number of column values.

!!! warning
    For tools related to specific tasks, please go to the respective documentation:

    - [Parsing text to table](tabletools/parse).

    - [Schema of table](tabletools/schema).

!!! warning
    For all the functions except [`loadcsv`](#loadcsv) and [`dumpcsv`](#dumpcsv), the header must be removed for best result.

## Table Transformation

Tools for table transformations.

### `transpose`

`transpose(data)` returns the transpose of table `data`, i.e., switch rows and columns.

!!! tip
    Useful to switch table `data` from row-based to column-based and backwards.

``` python
list(transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
# [(1, 4, 7),
#  (2, 5, 8),
#  (3, 6, 9)]
```

### `trim`

`trim(table, blank=None`) removes any empty column or row.

- `blank=None` is a list of characters denoting empty value. Default to whitespace characters.

!!! tip
    Check the builtin function [`str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) for details of the behavior with `blank`.

``` python
list(trim([
    ['', 'a', 'b'],
    ['', '-', '-'],
    ['', 'c', 'd']
], blank='-'))
# [['a', 'b'],
#  ['c', 'd']]
```

### `mergecols`

`mergecols(cols, default=None, blank=None)` merges the columns in `cols` into a single column. Returns `None` if there is conflict in any row.

- A row has conflict if there are more than one valid values, where each valid value is not `None` or empty.

    - `blank=None` is a list of characters denoting empty value. Default to whitespace characters.

- `default` is a placeholder when there are no valid value in one row.

!!! tip
    Check the builtin function [`str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) for details of the behavior with `blank`.

``` python
cols = list(transpose([
    [   0, None,    2, None],
    [   0,    1, None, None],
    [None,    1, None, None],
    [   0, None, None, None]
]))

# Merge the last two columns.
mergecols(cols[1:])
# [2,
#  1,
#  1,
#  None]

# Merge all three columns.
mergecols(cols)
# None
```

### `sortedbycol`

`sortedbycol(data, key=None)` sorts the columns of table `data` according to key function `key` over each column.

``` python
list(sortedbycol([
    ["c1", "b1", "a2", "d1"],
    ["c2", "b1", "a1", "d1"],
], key=lambda col: col[0]))
# [('a2', 'b1', 'c1', 'd1'),
#  ('a1', 'b1', 'c2', 'd1')]
```

### `filterbycol`

`filterbycol(data, key=None)` filters the columns of table `data` according to key function `key` over each column.

``` python
list(filterbycol([
    ["c1", "b1", "a2", "d1"],
    ["c2", "b1", "a1", "d1"],
], key=lambda col: len(set(col)) > 1))
# [('c1', 'a2'),
#  ('c2', 'a1')]
```

## Table Join

Tools for join tables.

### `join`

`join(lefttable, righttable, leftkey, rightkey, leftjoin=False, rightjoin=False)` [joins](https://en.wikipedia.org/wiki/Join_(SQL)) two tables `lefttable` and `righttable`, according to their respective keys `leftkey` and `rightkey`.

- Each key is a tuple of column IDs.

- `leftjoin` and `rightjoin` control whether to perform inner join, left outer join, right outer join, or full outer join.

!!! danger
    Both tables must be non-empty.

!!! info
    This function is a thin wrapper of [`seqtools.join`](seqtools#join). Please refer to `seqtools.join` for other join scenarios.

!!! tip
    Please refer to [`candidatekeys`](tabletools/schema#candidatekeys) and [`foreignkeys`](tabletools/schema#foreignkeys) on how to find primary/foreign-key automatically to join tables.

``` python
pt = [
    ["a1", "b1", "c1", "d1"],
    ["a1", "b1", "c2", "d1"],
    ["a2", "b1", "c1", "d1"],
]
pk = (0, 2)

ft = [
    ["c1", "b1", "a2", "d1"],
    ["c2", "b1", "a1", "d1"],
]
fk = (2, 0)

list(join(pt, ft, pk, fk))
# [(['a2', 'b1', 'c1', 'd1'], ['c1', 'b1', 'a2', 'd1']),
#  (['a1', 'b1', 'c2', 'd1'], ['c2', 'b1', 'a1', 'd1'])]

list(join(pt, ft, pk, fk, leftjoin=True))
# [(['a2', 'b1', 'c1', 'd1'], ['c1', 'b1', 'a2', 'd1']),
#  (['a1', 'b1', 'c2', 'd1'], ['c2', 'b1', 'a1', 'd1']),
#  (['a1', 'b1', 'c1', 'd1'], [None, None, None, None])]

list(join(pt, ft, pk, fk, rightjoin=True))
# [(['a2', 'b1', 'c1', 'd1'], ['c1', 'b1', 'a2', 'd1']),
#  (['a1', 'b1', 'c2', 'd1'], ['c2', 'b1', 'a1', 'd1'])]

list(join(pt, ft, pk, fk, leftjoin=True, rightjoin=True))
# [(['a2', 'b1', 'c1', 'd1'], ['c1', 'b1', 'a2', 'd1']),
#  (['a1', 'b1', 'c2', 'd1'], ['c2', 'b1', 'a1', 'd1']),
#  (['a1', 'b1', 'c1', 'd1'], [None, None, None, None])]
```

## CSV

Tools for processing CSV.

### `loadcsv`

`loadcsv(path, delimiter=',')` loads a CSV file, from either a file path, a file object, or an iterable of strings.

``` python
s = """Los Angeles,34°03′,118°15′
New York City,40°42′46″,74°00′21″
Paris,48°51′24″,2°21′03″"""

list(loadcsv(s.split('\n')))
# [['Los Angeles'  , '34°03′'   , '118°15′'  ],
#  ['New York City', '40°42′46″', '74°00′21″'],
#  ['Paris'        , '48°51′24″', '2°21′03″' ]]
```

### `dumpcsv`

`dumpcsv(path, data, delimiter=',')` dumps a table `data` in CSV, to either a file path or a file object.
