#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import operator
import itertools
from itertools import zip_longest, repeat
import math
from functools import lru_cache

from toolz import itertoolz
from toolz.itertoolz import sliding_window

from .misctools import cmp
from .dicttools import nextentries
from .__join import join

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


def commonsubseq(a: List[T], b: List[T]) -> List[T]:
    @lru_cache(maxsize=None)
    def align_rec(alen, blen):
        if alen == 0 or blen == 0 or a[alen - 1] != b[blen - 1]:
            return []

        return align_rec(alen - 1, blen - 1) + [a[alen - 1]]


    return max(
        (
            align_rec(i, j)
            for i in range(0, len(a) + 1)
            for j in range(0, len(b) + 1)
        ),
        key=len
    )


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


def commonsubseqwithgap(a: List[T], b: List[T]) -> List[T]:
    return [x for x, y in zip(*(align(a, b)[1])) if x == y]


def align(
        a: List[T], b: List[T],
        cost: Callable[[T, T], float] = None, bound: float = math.inf,
        default: T = None
    ) -> Tuple[float, Tuple[List[T], List[T]]]:
    def merge(prev, curr):
        if not prev:
            return None

        prevcost, (l, r) = prev
        x, y = curr

        currcost = prevcost + cost(x, y)
        if currcost > bound:
            return None

        return (currcost, (l + [x], r + [y]))


    @lru_cache(maxsize=None)
    def align_rec(alen, blen):
        if alen == 0 or blen == 0:
            res = (
                [default] * blen, b[:blen]
            ) if alen == 0 else (
                a[:alen], [default] * alen,
            )

            return (
                sum(cost(x, y) for x, y in zip(*res)),
                res
            )

        return min(
            (
                merge(align_rec(alen - 1, blen), (a[alen - 1], default)),
                merge(align_rec(alen, blen - 1), (default, b[blen - 1])),
                merge(align_rec(alen - 1, blen - 1), (a[alen - 1], b[blen - 1]))
            ),
            key=lambda x: x[0] if x else math.inf,
            default=None
        )


    if not cost:
        cost = lambda x, y: 0 if x == y else 1

    return align_rec(len(a), len(b))


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
