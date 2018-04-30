#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from toolz.itertoolz import groupby

class DisjointSets(Generic[T]):
    def __init__(self, *objs: T) -> None:
        self.weights: Dict[T, int] = {}
        self.parents: Dict[T, T] = {}
        self.numofsets = 0

        for obj in objs:
            self.add(obj)


    def __iter__(self):
        return iter(self.parents)


    def __contains__(self, obj: T) -> bool:
        return obj in self.parents


    def __len__(self) -> int:
        return len(self.parents)


    def add(self, obj: T) -> bool:
        if obj in self.parents:
            return False

        self.parents[obj] = obj
        self.weights[obj] = 1
        self.numofsets += 1

        return True


    def __getitem__(self, obj: T) -> T:
        if obj not in self:
            raise KeyError

        # Find path of objects up to the root
        path: List[T] = []

        root = obj
        while len(path) == 0 or root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # Compress the path
        for obj in path:
            self.parents[obj] = root

        return root


    def disjoints(self) -> Mapping[T, Iterable[T]]:
        return groupby(self.__getitem__, self.parents)


    def union(self, *objs: T) -> T:
        roots = [self[obj] for obj in objs]

        heaviest = max(roots, key=lambda r: self.weights[r])

        for r in roots:
            if r is heaviest or self.parents[r] is heaviest:
                continue

            self.weights[heaviest] += self.weights[r]
            self.parents[r] = heaviest
            self.numofsets -= 1

        return heaviest
