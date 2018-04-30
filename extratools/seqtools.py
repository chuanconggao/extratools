#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from itertools import zip_longest

from toolz.itertoolz import sliding_window

from .misctools import cmp

def findsubseq(a: Iterable[T], b: Iterable[T]) -> int:
    x = list(a)
    if len(x) == 0:
        return 0

    for pos, y in enumerate(sliding_window(len(x), b)):
        if all(m == n for m, n in zip(x, y)):
            return pos

    return -1


def issubseq(a: Iterable[T], b: Iterable[T]) -> bool:
    return findsubseq(a, b) >= 0


def findsubseqwithgap(a: Iterable[T], b: Iterable[T]) -> List[int]:
    sentinel = object()

    x, y = iter(a), iter(b)

    m: Any = sentinel
    n: Any = sentinel

    poss = []

    pos = -1
    while True:
        m, n = next(x, sentinel) if m is sentinel else m, next(y, sentinel)
        if m is sentinel or n is sentinel:
            break

        pos += 1

        if m == n:
            m = sentinel
            poss.append(pos)

    return poss if m is sentinel else None


def issubseqwithgap(a: Iterable[T], b: Iterable[T]) -> bool:
    return findsubseqwithgap(a, b) is not None


def productcmp(x: Iterable[T], y: Iterable[T]) -> int:
    lc, gc = 0, 0

    sentinel = object()

    for u, v in zip_longest(x, y, fillvalue=sentinel):
        if u is sentinel or v is sentinel:
            raise ValueError

        if u < v:
            lc += 1
        elif u > v:
            gc += 1

        if lc > 0 and gc > 0:
            return None

    return cmp(lc, gc)


def sortedbyrank(sth: Iterable[T], ranks: Iterable[float], reverse: bool = False) -> List[T]:
    return [
        v for _, v in sorted(
            zip(ranks, sth),
            reverse=reverse
        )
    ]
