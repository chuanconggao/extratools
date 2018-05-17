[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

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
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

### `mergecols`

`mergecols(cols, default=None)` merges the columns in `cols` into a single column. Returns `None` if there is conflict in any row.

- A row has conflict if there are more than one valid values, where each valid value is not `None` or empty string.

- `default` is a place holder when there are no valid value in one row.

``` python
cols = list(transpose([
    [   0, None,    2],
    [   0,    1, None],
    [None,    1, None]
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

## CSV

Tools for processing CSV.

### `loadcsv`

`loadcsv(path, delimiter=',')` loads a CSV file, from either a file path or a file object.

### `dumpcsv`

`dumpcsv(path, data, delimiter=',')` dumps a table `data` in CSV, to either a file path or a file object.

## Parsing Text to Table

Tools for parsing each line of text to a row in respective table.

### `parse`

`parse(lines, sep=None)` parses each line to a row by using separator `sep=None`.

!!! tip
    Check the builtin function [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split) for details of the behavior with `sep`.

``` python
list(parse([
    "1 ALICE Pairs",
    "2 BOB London"
]))
# [['1', 'ALICE',  'Pairs'],
#  ['2',   'BOB', 'London']]
```

### `parsebyregex`

`parsebyregex(lines, regex)` parses each line to a row by using a regular expression `regex`, where each capturing group matches a column value.

- `regex` can be either a regular expression string, or a regular expression object (compiled by either `re` or [`regex`](https://pypi.org/project/regex/)) for more advanced usage.

!!! tip
    Compatible third party library [`regex`](https://pypi.org/project/regex/) is used instead of standard library `re`, to support advanced unicode features.

``` python
list(parsebyregex(
    [
        "1 ALICE Pairs",
        "2 BOB London",
        "3 CARL JR New York"
    ],
    r"\s+".join([
        r"(\d+)",
        r"([A-Z]+(?:\s+[A-Z]+)*)",
        r"(.+)"
    ])
))
# [('1',   'ALICE',    'Pairs'),
#  ('2',     'BOB',   'London'),
#  ('3', 'CARL JR', 'New York')]
```

### `parsebyregexes`

`parsebyregexes(lines, regexes)` parses each line to a row by using a list of regular expressions `regexes`, where each regular expression matches a column value.

- Each regular expression of `regexes` can be either a regular expression string, or a regular expression object (compiled by either `re` or [`regex`](https://pypi.org/project/regex/)) for more advanced usage.

!!! tip
    Compatible third party library [`regex`](https://pypi.org/project/regex/) is used instead of standard library `re`, to support advanced unicode features.

``` python
list(parsebyregexes(
    [
        "1 ALICE Pairs",
        "2 BOB London",
        "3 CARL JR New York"
    ],
    [
        r"\b\d\b",
        r"\b[A-Z]+(?:\s+[A-Z]+)*\b",
        r"\b\S.+\b"
    ]
))
# [['1',   'ALICE',    'Pairs'],
#  ['2',     'BOB',   'London'],
#  ['3', 'CARL JR', 'New York']]
```
