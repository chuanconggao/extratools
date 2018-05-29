!!! warning
    For all the functions except [`hasheader`](#hasheader), the header must be removed for best result.

## Column Types

Tools for processing column types.

### `inferschema`

`inferschema(data)` infers the schema of the table `data`, as a tuple of column types. Currently available types are listed as follows.

![Types](https://raw.githubusercontent.com/chuanconggao/RegexOrder/master/templates.svg?sanitize=true)

!!! info
    Utilizes the [`RegexOrder`](https://github.com/chuanconggao/RegexOrder) library to infer the type of each column.

    `RegexOrder` is part of a research project. Thus, when using this function for research purpose, please cite both [`RegexOrder`](https://github.com/chuanconggao/RegexOrder#reference) and [`extratools`](../README#reference) accordingly.

``` python
inferschema([
    ['Los Angeles'  , '34°03′'   , '118°15′'  ],
    ['New York City', '40°42′46″', '74°00′21″'],
    ['Paris'        , '48°51′24″', '2°21′03″' ]
])
# ('title_words', 'formated_pos_ints', 'formated_pos_ints')
```

### `hasheader`

`hasheader(data)` returns the confidence (between $0$ and $1$) of whether the first row of the table `data` is header.

!!! info
    It works by checking whether the type with vs. without the first row for each column, using the [`RegexOrder`](https://github.com/chuanconggao/RegexOrder) library.

    `RegexOrder` is part of a research project. Thus, when using this function for research purpose, please cite both [`RegexOrder`](https://github.com/chuanconggao/RegexOrder#reference) and [`extratools`](../README#reference) accordingly.

``` python
t = [
    ['Los Angeles'  , '34°03′'   , '118°15′'  ],
    ['New York City', '40°42′46″', '74°00′21″'],
    ['Paris'        , '48°51′24″', '2°21′03″' ]
]

hasheader(t)
# 0.0

hasheader([
    ['City', 'Latitude', 'Longitude']
] + t)
# 0.6666666666666666

hasheader([
    ['C1', 'C2', 'C3']
] + t)
# 1.0
```

## Primary/Foreign-Key of Table

Tools for processing primary/foreign-key of table.

### `candidatekeys`

`candidatekeys(data, maxcols)` finds the [candidate keys](https://en.wikipedia.org/wiki/Candidate_key) of a table `data`.

- In default, the maximum number of columns `maxcols` in each candidate key is limited to `1` for efficiency. Specify larger number for more accurate results.

- Each candidate key is a tuple of column IDs.

!!! note
    A proper primary key is further selected from the candidate keys.

``` python
t1 = [
    ["a1", "b1", "c1", "d1"],
    ["a2", "b1", "c2", "d1"],
    ["a3", "b1", "c1", "d1"],
]

list(candidatekeys(t1))
# [(0,)]
list(candidatekeys(t1, maxcols=4))
# [(0,)]


t2 = [
    ["a1", "b1", "c1", "d1"],
    ["a1", "b1", "c2", "d1"],
    ["a2", "b1", "c1", "d1"],
]

list(candidatekeys(t2))
# []
list(candidatekeys(t2, maxcols=4))
# [(0, 2)]
```

### `foreignkeys`

`foreignkeys(primarydata, primarykey, foreigndata)` finds the [foreign keys](https://en.wikipedia.org/wiki/Foreign_key) of the foreign table `foreigndata`, according to the primary key `primarykey` of the primary table `primarydata`.

- Each foreign key is a tuple of column IDs.

``` python
pt = [
    ["a1", "b1", "c1", "d1"],
    ["a1", "b1", "c2", "d1"],
    ["a2", "b1", "c1", "d1"],
]

# Primary key of table tp
pk = list(candidatekeys(pt, maxcols=4))[0]
# (0, 2)

ft = [
    ["c1", "b1", "a2", "d1"],
    ["c2", "b1", "a1", "d1"],
]

# Foreign keys of table ft
list(foreignkeys(pt, pk, ft))
# [(2, 0)]
```
