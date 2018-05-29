Tools for encoding/decoding sequences.

### `compress`

`compress(data, key=None)` compresses the sequence `data` by encoding continuous identical items to a tuple of item and count, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

!!! warning
    Different from [`itertools.compress`](https://docs.python.org/3.6/library/itertools.html#itertools.compress).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

### `decompress`

`decompress(data)` decompresses the sequence `data` by decoding each tuple of item and count to continuous identical items, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

``` python
list(decompress([(1, 1), (2, 2), (3, 3), (4, 4)]))
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

### `todeltas`

`todeltas(data, op=operator.sub)` compresses the sequence by encoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

- For custom type of item, either define the `-` operator or specify the `op` function computing the difference.

``` python
list(todeltas([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
```

### `fromdeltas`

`fromdeltas(data, op=operator.add)` decompresses the sequence by decoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

- For custom type of item, either define the `+` operator or specify the `op` function merging the difference.

``` python
list(fromdeltas([1, 1, 0, 1, 0, 0, 1, 0, 0, 0]))
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```


