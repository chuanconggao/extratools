[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/printtools.py)

## Printing

Tools for non-functional but useful printing purposes.

### `print2(*args, **kwargs)`

Redirects the output of `print` to standard error.

- The same parameters are accepted.

### `iter2str(seq, limit=None)`

Converts an iterable sequence to string.

- If `limit` is specified, only print the first `limit` items. This is useful when `seq` is an infinite sequence.

- Builtin function `repr` is used to print each item safely.

``` python
iter2str(range(5))
# '<0, 1, 2, 3, 4>'

# Infinity sequence
iter2str(itertools.count(), limit=5)
# '<0, 1, 2, 3, 4, ...>'
```

### `alignment2str(*seqs, default=None)` and `table2str(data, default=None)`

Prints the alignment between sequences `seq`. `default=None` is used for labelling missing value from each sequences.

- `table2str` is a thin wrapper of `alignment2str` to print a row-based table.

- If unknown, `seqtools.align` can compute the alignment between two sequences.

- Builtin function `repr` is used to print each item safely.

- If sequences have different lengths, the extra trailing items are also printed as not matching.

``` python
print(alignment2str(
    [1, 10,  100, "New York"],
    [1, 10, None, "New York"]
))
1 10 100 'New York'
1 10     'New York'

print(alignment2str(*align(
    [1, 10, 100, "New York"],
    [1, 10,      "New York"]
)[1]))
1 10 100 'New York'
1 10     'New York'

print(alignment2str(
    [1, 10, 100, "New York"],
    [1, 10, 100]
))
1 10 100 'New York'
1 10 100     

print(table2str([
    [1,   10,  100, "New York"],
    [1,   10, None, "New York"],
    [1, None,  100, "New York"],
    [1,   10,  100, "New York"]
]))
1 10 100 'New York'
1 10     'New York'
1    100 'New York'
1 10 100 'New York'
```
