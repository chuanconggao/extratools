#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

def sortedcommon(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = lambda v: v
    ) -> Iterable[T]:
    sentinel = object()

    x, y = iter(a), iter(b)

    m: Any = sentinel
    n: Any = sentinel

    while True:
        m = next(x, sentinel) if m is sentinel else m
        n = next(y, sentinel) if n is sentinel else n

        if m is sentinel or n is sentinel:
            break

        if key(m) < key(n):
            m = sentinel
        elif key(m) > key(n):
            n = sentinel
        else:
            yield m
            m = n = sentinel


def sorteddiff(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = lambda v: v
    ) -> Iterable[T]:
    sentinel = object()

    x, y = iter(a), iter(b)

    m: Any = sentinel
    n: Any = sentinel

    while True:
        m = next(x, sentinel) if m is sentinel else m
        n = next(y, sentinel) if n is sentinel else n

        if m is sentinel or n is sentinel:
            break

        if key(m) < key(n):
            yield m
            m = sentinel
        elif key(m) > key(n):
            yield n
            n = sentinel
        else:
            m = n = sentinel

    while m is not sentinel:
        yield m

        m = next(x, sentinel)

    while n is not sentinel:
        yield n

        n = next(y, sentinel)
