Tools for set similarities.

### `jaccard`

`jaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`.

``` python
jaccard(
    {1, 2, 3   },
    {1,    3, 5}
)
# 0.5 = 2 / 4
```

### `multisetjaccard`

`multisetjaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two multi-sets (Counters) `a` and `b`.

``` python
multisetjaccard(
    Counter([1, 1, 2, 3   ]),
    Counter([1,       3, 5])
)
# 0.4 = 2 / 5
```

### `weightedjaccard`

`weightedjaccard(a, b, key=sum)` computes the weighted [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`, using function `key` to compute the total weight of the elements within a set.

``` python
weightedjaccard(
    {1, 2, 3   },
    {1,    3, 5}
)
# 0.36363636363636365 = (1 + 3) / (1 + 2 + 3 + 5) = 4 / 11

weightedjaccardjaccard(
    {1, 2, 3   },
    {1,    3, 5},
    key=len
)
# 0.5 = 2 / 4

weightedjaccard(
    Counter([1, 1, 2, 3   ]),
    Counter([1,       3, 5]),
    key=lambda c: sum(c.values())
)
# 0.4 = 2 / 5
```
