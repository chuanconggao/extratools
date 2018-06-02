[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/graphtools.py)

## PageRank

Tools for computing PageRank of a graph.

### `approxpagerank`

`approxpagerank(objs, func)` approximates the PageRank of nodes `objs` in an undirected graph, where the weight of each edge is computed by function `func`.

!!! info
    According to [Wikipedia](https://en.wikipedia.org/wiki/PageRank#PageRank_of_an_undirected_graph), the PageRank of an undirected graph is statistically close to its degree distribution.

``` python
approxpagerank(
    [
        "apple",
        "apple pie",
        "banana",
        "cherry pie"
    ],
    lambda a, b: settools.jaccard(set(a.split()), set(b.split()))
)
# [0.5,
#  0.8333333333333333,
#  0,
#  0.3333333333333333]
```
