[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/segmenttree.py)

This data structure solves the [range minimum query problem](https://en.wikipedia.org/wiki/Range_minimum_query) of finding the minimal value in a sub-array of an array of comparable objects. Different from the original problem, this data structure also supports updating the values.

### Initialization

Use `SegmentTree()` to initialize the tree with a set of keys, in **comparable and hashable** type.

- `func=min` specifies how the best value is computed for any range of keys.

- `default=None` specifies the default value for each key.

- `numchild=2` specifies the maximum number of children for each node.

!!! info
    The space complexity is $O(n)$. The time complexity is $O(n \cdot \log n)$.

``` Python
tree = SegmentTree(
    {1, 2, 3, 4, 5},
    func=min, default=0
)
```

### Updating

Use `update(keyvals)` to initialize the values, or update the values if necessary, by specifying `(Key, Value)` pairs `keyvals`.

!!! warning
    Currently, adding new keys is not supported yet.

!!! info
    Given m values updated, the time complexity should be $O(m \cdot \log n)$.

``` Python
tree.update({1: 3, 2: -1, 4: 6})
```

### Querying

Use `query(queryrange)` to to find the best value of a range of keys `queryrange`.

!!! warning
    The range here is closed on the left side and open on the right side, consistent with [`rangetools`](../functions/rangetools).

!!! info
    The time complexity should be $O(log n)$.

``` Python
tree.query((1, 3))
# -1
```
