[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/printtools.py)

## Printing

Tools for non-functional but useful printing purposes.

### `print2(*args, **kwargs)`

Redirects the output of `print` to standard error.

- The same parameters are accepted.

### `iter2str(seq, limit=None)`

Converts an iterable sequence to string.

- If `limit` is specified, only print the first `limit` items. This is useful when `seq` is an infinite sequence.

``` python
iter2str(range(5))
# '<0, 1, 2, 3, 4>'

# Infinity sequence
iter2str(itertools.count(), limit=5)
# '<0, 1, 2, 3, 4, ...>'
```

### `alignment2str(a, b, default=None)`

Prints the alignment between two sequences `a` and `b`. `default=None` is used for labelling missing value from each sequences.

- If unknown, `seqtools.align` can compute the alignment between `a` and `b`.

- Builtin function `repr` is used to print each item safely.

- If `a` and `b` have different lengths, the extra trailing items are also printed as not matching.

``` python
print(alignment2str(
    [1, 10,  100, 1000],
    [1, 10, None, 1000]
))
1 10 100 1000
1 10     1000

print(alignment2str(*align(
    [1, 10, 100, 1000],
    [1, 10,      1000]
)[1]))
1 10 100 1000
1 10     1000

print(alignment2str(
    [1, 10, 100, 1000],
    [1, 10, 100]
))
1 10 100 1000
1 10 100     
```
