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
