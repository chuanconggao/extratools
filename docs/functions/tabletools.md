[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

## Table Transformation

Tools for table transformations.

### `transpose(data)`

Returns the transpose of table `data`, i.e., switch rows and columns.

!!! tip
    Useful to switch table `data` from row-based to column-based and backwards.

``` python
list(transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

## CSV

Tools for processing CSV.

### `loadcsv(path, delimiter=',')`

Loads a CSV file, from either a file path or a file object.

### `dumpcsv(path, data, delimiter=',')`

Dumps a table `data` in CSV, to either a file path or a file object.
