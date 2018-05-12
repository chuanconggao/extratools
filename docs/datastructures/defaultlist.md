[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/defaultlist.py)

A sub-class of `list` that automatically grows when setting an index beyond the list size.

- When creating a list, use `DefaultList(default, ...)` to specify a function that returns default value when visiting an unassigned index.

!!! tip
    This library is designed to be highly similar to `collections.defaultdict` in standard library.

``` python
l = DefaultList(lambda: None, range(10))

l[11] = 11

l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11]
```

