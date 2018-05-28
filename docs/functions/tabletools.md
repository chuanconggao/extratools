[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

!!! info
    A table is a list of rows having the same number of column values.

!!! warning
    For tools related to specific tasks, please go to the respective documentation:

    - [Parsing text to table](tabletools/parse).

    - [Schema of table](tabletools/schema).

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

### `mergecols`

`mergecols(cols, default=None, blank=None)` merges the columns in `cols` into a single column. Returns `None` if there is conflict in any row.

- A row has conflict if there are more than one valid values, where each valid value is not `None` or empty.

    - `blank=None` is a list of characters denoting empty value. Default to whitespace characters.

- `default` is a placeholder when there are no valid value in one row.

!!! tip
    Check the builtin function [`str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) for details of the behavior with `blank`.

``` python
cols = list(transpose([
    [   0, None,    2],
    [   0,    1, None],
    [None,    1, None],
    [0,    None, None]
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
