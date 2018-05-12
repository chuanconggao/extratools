#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from heapq import merge
from itertools import groupby, zip_longest

from toolz.itertoolz import count, unique, sliding_window

from .__join import __sortedjoin, sortedjoin

def sortedcommon(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    for m, n in __sortedjoin(
            a, b,
            leftkey=key, rightkey=key
        ):
        yield from min(m, n, key=len)


def sortedalone(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    sentinel = object()

    for m, n in __sortedjoin(
            a, b,
            leftkey=key, rightkey=key,
            leftdefault=sentinel, rightdefault=sentinel
        ):
        if m[0] is sentinel:
            yield from n
        elif n[0] is sentinel:
            yield from m
        else:
            if len(m) > len(n):
                yield from m[len(n):]
            elif len(m) < len(n):
                yield from n[len(m):]


def sorteddiff(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    sentinel = object()

    for m, n in __sortedjoin(
            a, b,
            leftkey=key, rightkey=key,
            rightdefault=sentinel
        ):
        if n[0] is sentinel:
            yield from m
        else:
            if len(m) > len(n):
                yield from m[len(n):]


def issubsorted(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    sentinel = object()

    return next(iter(sorteddiff(a, b, key=key)), sentinel) is sentinel


def sortedmatch(
        a: List[T], b: List[T],
        default: T = None
    ) -> Tuple[List[T], List[T]]:
    sentinel = object()

    for m, n in __sortedjoin(
            a, b,
            leftdefault=sentinel, rightdefault=sentinel
        ):
        if m[0] is sentinel:
            for v in n:
                yield (default, v)
        elif n[0] is sentinel:
            for v in m:
                yield (v, default)
        else:
            for v, w in zip_longest(m, n, fillvalue=default):
                yield (v, w)


def issorted(
        seq: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    if key is None:
        key = lambda v: v

    return all(
        key(prev) <= key(curr)
        for prev, curr in sliding_window(2, seq)
    )


def matchingfrequencies(*seqs: Iterable[T], key=None) -> Iterable[Tuple[T, int]]:
    for k, g in groupby(merge(
            *[unique(seq, key=key) for seq in seqs],
            key=key
        )):
        yield (k, count(g))
