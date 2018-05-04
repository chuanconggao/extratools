#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import operator
import itertools
from itertools import zip_longest, repeat

from collections import defaultdict

from toolz import itertoolz
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


def findsubseqwithgap(a: Iterable[T], b: Iterable[T]) -> Optional[List[int]]:
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


Entries = List[Tuple[int, int]]

def nextentries(data: List[List[T]], entries: Entries) -> Mapping[T, Entries]:
    entriesDict: Mapping[T, Entries] = defaultdict(list)

    for i, lastpos in entries:
        seq = data[i]

        for pos in range(lastpos + 1, len(seq)):
            l = entriesDict[seq[pos]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, pos))

    return entriesDict


def productcmp(x: Iterable[T], y: Iterable[T]) -> Optional[int]:
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


def sortedbyrank(data: Iterable[T], ranks: Iterable[float], reverse: bool = False) -> List[T]:
    return [
        v for _, v in sorted(
            zip(ranks, data),
            reverse=reverse
        )
    ]


def compress(data: Iterable[T], key: Callable[[T], Any] = None) -> Iterable[Tuple[T, int]]:
    for k, g in itertools.groupby(data, key=key):
        yield (k, itertoolz.count(g))


def decompress(data: Iterable[Tuple[T, int]]) -> Iterable[T]:
    for k, n in data:
        yield from repeat(k, n)


def todeltas(data: Iterable[T], op: Callable[[T, T], T] = operator.sub) -> Iterable[T]:
    sentinel = object()

    seq = iter(data)

    curr: Any = next(seq, sentinel)
    if curr is sentinel:
        return

    yield curr

    prev = curr

    for curr in seq:
        yield op(curr, prev)

        prev = curr


def fromdeltas(data: Iterable[T], op: Callable[[T, T], T] = operator.add) -> Iterable[T]:
    sentinel = object()

    seq = iter(data)

    curr: Any = next(seq, sentinel)
    if curr is sentinel:
        return

    yield curr

    prev = curr

    for curr in seq:
        curr = op(prev, curr)
        yield curr

        prev = curr
