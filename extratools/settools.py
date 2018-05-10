#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from .seqtools import bestsubseqwithgap
from .mathtools import safediv

def bestsubset(a: Set[T], key: Callable[[Iterable[T]], Any]) -> Set[T]:
    return set(bestsubseqwithgap(list(a), key))


def addtoset(s: Set[T], x: T) -> bool:
    if x in s:
        return False

    s.add(x)
    return True


def weightedjaccard(a: Any, b: Any, key: Callable[[Any], float] = sum) -> float:
    x = key(a & b)
    return safediv(x, key(a) + key(b) - x)


def jaccard(a: Set[T], b: Set[T]) -> float:
    return weightedjaccard(a, b, key=len)


def multisetjaccard(a: Counter[T], b: Counter[T]) -> float:
    return weightedjaccard(a, b, key=lambda c: sum(c.values()))
