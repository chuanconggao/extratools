[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

Tools for tables.

- `transpose(data)` returns the transpose of table `data`, i.e., switch rows and columns.

    - Useful to switch table `data` from row-based to column-based and backwards.

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

- `loadcsv(path, delimiter=',')` loads a CSV file, from either a file path or a file object.

- `dumpcsv(path, data, delimiter=',')` dumps a table `data` in CSV, to either a file path or a file object.
