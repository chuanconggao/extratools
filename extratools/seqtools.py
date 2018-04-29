#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from toolz.itertoolz import sliding_window

def issubseq(a: Iterable[T], b: Iterable[T]) -> bool:
    x = list(a)

    return any(
        all(m == n for m, n in zip(x, y))
        for y in sliding_window(len(x), b)
    )


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
