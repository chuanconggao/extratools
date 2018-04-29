#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from itertools import zip_longest

from toolz.itertoolz import sliding_window

from .misctools import cmp

def findsubseq(a: Iterable[T], b: Iterable[T]) -> int:
    x = list(a)

    for pos, y in enumerate(sliding_window(len(x), b)):
        if all(m == n for m, n in zip(x, y)):
            return pos

    return -1


def issubseq(a: Iterable[T], b: Iterable[T]) -> bool:
    return findsubseq(a, b) >= 0


def issubseqwithgap(a: Iterable[T], b: Iterable[T]) -> bool:
    sentinel = object()

    x, y = iter(a), iter(b)

    m: Union[T, object] = sentinel
    n: Union[T, object] = sentinel

    while True:
        m, n = m or next(x, sentinel), next(y, sentinel)
        if m is sentinel or n is sentinel:
            break

        if m == n:
            m = sentinel

    return m is sentinel


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
