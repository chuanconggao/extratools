#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from .__join import sortedjoin

def __sortedscan(
        adiff: bool, bdiff: bool,
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    if key is None:
        key = lambda v: v

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
            if adiff:
                yield m
            m = sentinel
        elif key(m) > key(n):
            if bdiff:
                yield n
            n = sentinel
        else:
            if not adiff and not bdiff:
                yield m
            m = n = sentinel

    if adiff:
        while m is not sentinel:
            yield m

            m = next(x, sentinel)

    if bdiff:
        while n is not sentinel:
            yield n

            n = next(y, sentinel)


def sortedcommon(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    return __sortedscan(False, False, a, b, key=key)


def sortedalone(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    return __sortedscan(True, True, a, b, key=key)


def sorteddiff(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    return __sortedscan(True, False, a, b, key=key)


def issubsorted(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    sentinel = object()

    return next(iter(sorteddiff(a, b, key=key)), sentinel) is sentinel


def issorted(
        a: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    if key is None:
        key = lambda v: v

    sentinel = object()

    seq = iter(a)

    prev = sentinel

    while True:
        curr = next(seq, sentinel)
        if curr is sentinel:
            return True

        if prev is not sentinel and key(prev) > key(curr):
            return False

        prev = curr
