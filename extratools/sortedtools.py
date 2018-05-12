#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from heapq import merge
from itertools import groupby

from toolz.itertoolz import count, unique, sliding_window

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
        seq: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    if key is None:
        key = lambda v: v

    for prev, curr in sliding_window(2, seq):
        if key(prev) > key(curr):
            return False

    return True


def matchingfrequencies(*seqs: Iterable[T], key=None) -> Iterable[Tuple[T, int]]:
    for k, g in groupby(merge(*[unique(seq, key=key) for seq in seqs], key=key)):
        yield (k, count(g))
