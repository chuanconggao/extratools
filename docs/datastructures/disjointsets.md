[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/disjointsets.py)

[Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) with path compression. After `d = DisjointSets()`:

- `d.add(x)` adds a new disjoint set containing `x`.

- `d[x]` returns the representing element of the disjoint set containing `x`.

- `d.disjoints()` returns all the representing elements and their respective disjoint sets.

- `d.union(*xs)` union all the elements in `xs` into a single disjoint set.

!!! note
    Based a lot on this [implementation](https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py)
