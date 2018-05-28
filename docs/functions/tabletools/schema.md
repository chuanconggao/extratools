## Schema of Table

Tools for processing schema of table.

!!! warning
    The header must be removed for best result.

### `inferschema`

`inferschema(table)` infers the schema of the table `table`, as a tuple of column types. Currently available types are listed as follows.

![Types](https://raw.githubusercontent.com/chuanconggao/RegexOrder/master/templates.svg?sanitize=true)

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
tp = [
    ["a1", "b1", "c1", "d1"],
    ["a1", "b1", "c2", "d1"],
    ["a2", "b1", "c1", "d1"],
]

# Primary key of table tp
pk = list(candidatekeys(tp, maxcols=4))[0]
# (0, 2)

tf = [
    ["c1", "b1", "a2", "d1"],
    ["c2", "b1", "a1", "d1"],
]

# Foreign keys of table tf
list(foreignkeys(tp, pk, tf))
# [(2, 0)]
```
