#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from .seqtools import bestsubseqwithgap
from .mathtools import safediv

def bestsubset(a: Set[T], key: Callable[[Iterable[T]], Any]) -> Set[T]:
    return set(bestsubseqwithgap(list(a), key))


def setcover(whole: Iterable[T], covered: Iterable[Set[T]], key: Callable = len) -> Iterable[FrozenSet[T]]:
    whole = set(whole)
    covers = set(frozenset(x) for x in covered)

    while len(whole) and len(covers):
        bestval, best = None, None
        for curr in covers:
            currtemp = curr & whole
            if len(currtemp):
                currval = key(currtemp)
                if not bestval or currval > bestval:
                    bestval, best = currval, curr

        if not best:
            return

        yield best

        whole -= best
        covers.remove(best)


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
