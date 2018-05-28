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

## Parsing Text to Table

Tools for parsing each line of text to a row in respective table.

### `parse`

`parse(lines, sep=None, useregex=False)` parses each line to a row by using separator `sep=None`.

- In default, `sep` is a plain string. When setting `useregex`, `sep` is a regular expression for more advanced scenarios.

!!! tip
    Check the builtin function [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split) for details of the behavior with `sep` when `useregex = False`.

``` python
list(parse([
    "1 ALICE Pairs",
    "2 BOB London"
]))
# [['1', 'ALICE',  'Pairs'],
#  ['2',   'BOB', 'London']]

list(parse([
    "1 | ALICE | Pairs",
    "2 | BOB | London"
], sep=r"\s*\|\s*", useregex=True))
# [['1', 'ALICE',  'Pairs'],
#  ['2',   'BOB', 'London']]
```

### `parsebymarkdown`

`parsebymarkdown(text)` parses a text of multiple lines to a table, according to [Markdown](https://github.github.com/gfm/#tables-extension-) format.

``` python
list(parsebymarkdown("""
| foo | bar |
| --- | --- |
| baz | bim |
"""))
# [['foo', 'bar'],
#  ['baz', 'bim']]
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

## Schema of Table

Tools for processing schema of table.

### `inferschema`

`inferschema(table)` infers the schema of the table `table`, as a tuple of column types. Currently available types are listed as follows.

![Types](https://raw.githubusercontent.com/chuanconggao/RegexOrder/master/templates.svg?sanitize=true)

!!! warning
    The header must be removed for best result.

!!! info
    Utilizes the [`RegexOrder`](https://github.com/chuanconggao/RegexOrder) library.

    `RegexOrder` is part of a research project. Thus, when using this function for research purpose, please cite both [`RegexOrder`](https://github.com/chuanconggao/RegexOrder#reference) and [`extratools`](../README#reference) accordingly.

``` python
t = [
    ['Los Angeles'  , '34°03′'   , '118°15′'  ],
    ['New York City', '40°42′46″', '74°00′21″'],
    ['Paris'        , '48°51′24″', '2°21′03″' ]
]

inferschema(t)
# ('title_words', 'formated_pos_ints', 'formated_pos_ints')
```

### `candidatekeys`

`candidatekeys(data, maxcols)` finds the [candidate keys](https://en.wikipedia.org/wiki/Candidate_key) of a table `data`.

- In default, the maximum number of columns `maxcols` in each candidate key is limited to `1` for efficiency. Specify larger number for more accurate results.

!!! note
    A proper primary key is further selected from the candidate keys.

``` python
t1 = [
    ["a1", "b1", "c1", "d1"],
    ["a2", "b1", "c2", "d1"],
    ["a3", "b1", "c1", "d1"],
]

list(candidatekeys(t1))
# [{0}]
list(candidatekeys(t1, maxcols=4))
# [{0}]


t2 = [
    ["a1", "b1", "c1", "d1"],
    ["a1", "b1", "c2", "d1"],
    ["a2", "b1", "c1", "d1"],
]

list(candidatekeys(t2))
# []
list(candidatekeys(t2, maxcols=4))
# [{0, 2}]
```
