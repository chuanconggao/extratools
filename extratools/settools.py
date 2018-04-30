#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from .mathtools import safediv

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
