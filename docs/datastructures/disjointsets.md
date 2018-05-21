[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/disjointsets.py)

[Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) with path compression. After `d = DisjointSets()`:

- `d[x]` returns the representing element of the disjoint set containing `x`.

- `d.add(x)` adds a new disjoint set containing `x` and returns the representing element of the disjoint set.

- `d.disjoints()` returns all the disjoint sets and their respective representing elements.

- `d.union(*xs)` unions all the elements in `xs` into a single disjoint set.

!!! note
    Based a lot on this [implementation](https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py)

``` python
d = DisjointSets()

for i in range(10):
    d.add(i)

d.disjoints()
# {0: [0],
#  1: [1],
#  2: [2],
#  3: [3],
#  4: [4],
#  5: [5],
#  6: [6],
#  7: [7],
#  8: [8],
#  9: [9]}

d.union(1, 2, 3)
# 1

d.union(2, 4)
# 1

d.union(5, 7, 9)
# 5

d.disjoints()
# {0: [0],
#  1: [1, 2, 3, 4],
#  5: [5, 7, 9],
#  6: [6],
#  8: [8]}
```
