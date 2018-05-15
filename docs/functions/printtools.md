[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/printtools.py)

## Printing

Tools for controlling printing destination.

### `print2`

`print2(*args, **kwargs)` redirects the output of `print` to standard error.

!!! tip
    The same parameters of builtin `print` are accepted.

## To String

Tools for generating the intuitive string representation.

!!! info
    Builtin function `repr` is used to print each item safely.


### `iter2str`

`iter2str(seq, limit=None)` converts an iterable sequence to string.

- If `limit` is specified, only print the first `limit` items. This is useful when `seq` is an infinite sequence.

``` python
iter2str(range(5))
# '<0, 1, 2, 3, 4>'

# Infinity sequence
iter2str(itertools.count(), limit=5)
# '<0, 1, 2, 3, 4, ...>'
```

### `alignment2str`

`alignment2str(*seqs, default=None, separator=' ')` prints the alignment between sequences `seq`. `default=None` is used for labelling missing value from each sequences.

- `separator` can be specified to separate every two values.

- If sequences have different lengths, the extra trailing items are also printed as not matching.

!!! tip
    `seqtools.align` can compute the alignment between two sequences.

``` python
print(alignment2str(
    [1, 10,  100, "New York"],
    [1, 10, None, "New York"]
))
# 1 10 100 'New York'
# 1 10     'New York'

print(alignment2str(*align(
    [1, 10, 100, "New York"],
    [1, 10,      "New York"]
)[1]))
# 1 10 100 'New York'
# 1 10     'New York'

print(alignment2str(
    [1, 10, 100, "New York"],
    [1, 10, 100]
))
# 1 10 100 'New York'
# 1 10 100     
```

### `table2str`

`table2str(data, default=None, separator=" | ")` a thin wrapper of `alignment2str` to print a row-based table.

!!! tip
    The default output format is compatible to Markdown format.

``` python
print(table2str([
    [1,   10,  100, "New York"],
    [1,   10, None, "New York"],
    [1, None,  100, "New York"],
    [1,   10,  100, "New York"]
]))
# 1 | 10 | 100 | 'New York'
# 1 | 10 |     | 'New York'
# 1 |    | 100 | 'New York'
# 1 | 10 | 100 | 'New York'
```

### `range2str`

`range2str(r)` prints a range `r`.

``` python
print(range2str((0, 1)))
# [0, 1)
```

### `sorted2str`

`sorted2str(seq, key=None)` prints a sorted sequence `seq`, optionally according to the key function `key`.

``` python
print(sorted2str([1, 2, 2, 3]))
# 1 <= 2 == 2 <= 3
```
