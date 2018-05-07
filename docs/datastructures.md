# Data Structures

<a name="disjointsets"></a>
## [`disjointsets.DisjointSets`](https://github.com/chuanconggao/extratools/blob/master/extratools/disjointsets.py)

[Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) with path compression, based a lot on this [implementation](https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py). After `d = DisjointSets()`:

- `d.add(x)` adds a new disjoint set containing `x`.

- `d[x]` returns the representing element of the disjoint set containing `x`.

- `d.disjoints()` returns all the representing elements and their respective disjoint sets.

- `d.union(*xs)` union all the elements in `xs` into a single disjoint set.

<a name="defaultlist"></a>
## [`defaultlist.defaultlist`](https://github.com/chuanconggao/extratools/blob/master/extratools/defaultlist.py)

A sub-class of `list` that automatically grows when setting an index beyond the list size.

- When creating a list, use `DefaultList(default, ...)` to specify a function that returns default value when visiting an unassigned index.

- This library is designed to be highly similar to `collections.defaultdict` in standard library.

``` python
l = DefaultList(lambda: None, range(10))

l[11] = 11

l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11]
```

<a name="segmenttree"></a>
## [`segmenttree.SegmentTree`](https://github.com/chuanconggao/extratools/blob/master/extratools/segmenttree.py)

This data structure solves the [range minimum query problem](https://en.wikipedia.org/wiki/Range_minimum_query) of finding the minimal value in a sub-array of an array of comparable objects. Different from the original problem, this data structure also supports updating the values.

### Initialization

Use `SegmentTree()` to initialize the tree with a set of keys, in **comparable and hashable** type.

- `func=min` specifies how the best value is computed for any range of keys.

- `default=None` specifies the default value for each key.

- `maxChildNum=2` specifies the maximum number of children for each node.

``` Python
tree = SegmentTree(
    {1, 2, 3, 4, 5},
    func=min, default=0, maxChildNum=2
)
```

The space complexity should be $O(n)$.

### Updating

You need to use `update()` to initialize the values, or update the values if necessary, by specifying a dictionary of key/value pairs. Currently, adding new keys is not supported yet.

``` Python
tree.update({1: 3, 4: 6})
```

Given m values updated, the time complexity should be $O(m^2)$.

### Querying

Use `query()` to to find the best value of a range of keys. The range is denoted by a tuple `(a, b)`, representing each key `x` such that `a <= x < b`. The range here is closed on the left side and open on the right side, consistent with Python tradition.

``` Python
tree.query((1, 3))
```

The time complexity should be $O(log n)$.

