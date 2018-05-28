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

