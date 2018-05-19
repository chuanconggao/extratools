#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import operator
import itertools
from itertools import chain, zip_longest, repeat, combinations
import math
from functools import lru_cache
from collections import defaultdict, Counter
from array import array

from toolz import itertoolz
from toolz.itertoolz import sliding_window, unique
from toolz.utils import no_default

from .misctools import cmp
from .dicttools import invertedindex, nextentries
from .__join import join

def iter2seq(a: Iterable[T], target=tuple) -> Sequence[T]:
    if isinstance(a, (list, str, tuple, array)):
        return a

    return target(a)


def bestsubseq(a: Iterable[T], key: Callable[[Iterable[T]], Any]) -> Iterable[T]:
    a = iter2seq(a)

    return max(
        chain([[]], (
            a[i:j]
            for i in range(len(a))
            for j in range(i + 1, len(a) + 1)
        )),
        key=key
    )


def findallsubseqs(a: Iterable[T], b: Iterable[T], overlap: bool = False) -> Iterable[int]:
    x = iter2seq(a)
    if len(x) == 0:
        return

    start = 0

    for pos, y in enumerate(sliding_window(len(x), b)):
        if (overlap or pos >= start) and all(m == n for m, n in zip(x, y)):
            yield pos
            start = pos + len(x)


def findsubseq(a: Iterable[T], b: Iterable[T]) -> int:
    x = iter2seq(a)
    if len(x) == 0:
        return 0

    return next(iter(findallsubseqs(a, b)), -1)


def issubseq(a: Iterable[T], b: Iterable[T]) -> bool:
    return findsubseq(a, b) >= 0


def commonsubseq(a: Iterable[T], b: Iterable[T]) -> Iterable[T]:
    @lru_cache(maxsize=None)
    # Find the start pos in list `a`
    def align_rec(alen, blen):
        if alen == 0 or blen == 0 or a[alen - 1] != b[blen - 1]:
            return alen

        return align_rec(alen - 1, blen - 1)

    a = iter2seq(a)
    b = iter2seq(b)

    for k in range(*max(
            (
                (align_rec(i, j), i)
                for i in range(0, len(a) + 1)
                for j in range(0, len(b) + 1)
            ),
            key=lambda x: x[1] - x[0]
        )):
        yield a[k]


def bestsubseqwithgap(a: Iterable[T], key: Callable[[Iterable[T]], Any]) -> Iterable[T]:
    def find(alen):
        if alen == 0:
            return (key([]), [])

        prevcost, prevseq = find(alen - 1)
        currseq = prevseq + [a[alen - 1]]

        return max(
            (prevcost, prevseq),
            (key(currseq), currseq),
            key=lambda x: x[0]
        )


    a = iter2seq(a)

    return find(len(a))[1]


def findallsubseqswithgap(a: Iterable[T], b: Iterable[T], overlap: bool = False) -> Iterable[List[int]]:
    def findallsubseqswithgap_overlap(prefixposs: List[int]) -> Iterable[List[int]]:
        if len(prefixposs) == len(x):
            yield prefixposs

            return

        first = x[len(prefixposs)]

        for i in range(prefixposs[-1] + 1 if len(prefixposs) else 0, len(y)):
            if y[i] != first:
                continue

            yield from findallsubseqswithgap_overlap(prefixposs + [i])


    x = iter2seq(a)
    if len(x) == 0:
        return

    y = cast(List, iter2seq(b, target=list))

    if overlap:
        yield from findallsubseqswithgap_overlap([])
        return

    sentinel = object()

    while True:
        poss = findsubseqwithgap(x, y)
        if poss is None:
            return

        yield poss

        for pos in poss:
            y[pos] = sentinel


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


def commonsubseqwithgap(a: Iterable[T], b: Iterable[T]) -> Iterable[T]:
    return (x for x, y in zip(*(align(a, b)[1])) if x == y)


def align(
        a: Iterable[T], b: Iterable[T],
        cost: Callable[[T, T], float] = None, bound: float = math.inf,
        default: T = None
    ) -> Tuple[float, Tuple[Iterable[T], Iterable[T]]]:
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


    a = iter2seq(a)
    b = iter2seq(b)

    if not cost:
        cost = lambda x, y: 0 if x == y else 1

    return align_rec(len(a), len(b))


def match(
        a: Iterable[T], b: Iterable[T],
        default: T = None
    ) -> Iterable[Tuple[T, T]]:
    return zip(*align(a, b, default=default)[1])


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


def sortedbyrank(data: Iterable[T], ranks: Iterable[Any], reverse: bool = False) -> Iterable[T]:
    return [
        v for _, v in sorted(
            zip(ranks, data),
            reverse=reverse
        )
    ]


def compress(data: Iterable[T], key: Optional[Callable[[T], Any]] = None) -> Iterable[Tuple[T, int]]:
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


def matchingfrequencies(*seqs: Iterable[T], key=None) -> Iterable[Tuple[T, int]]:
    c: Counter[T] = Counter()
    for seq in seqs:
        c.update(unique(seq, key=key))

    return c.items()


def enumeratesubseqs(seq: Iterable[T]) -> Iterable[Iterable[T]]:
    seq = iter2seq(seq)
    l = len(seq)

    for i in range(l):
        for j in range(i + 1, l + 1 if i > 0 else l):
            yield seq[i:j]


def enumeratesubseqswithgap(seq: Iterable[T]) -> Iterable[Iterable[T]]:
    seq = iter2seq(seq)

    for i in range(1, len(seq)):
        yield from combinations(seq, i)


def nonsharingsubseqs(*seqs: Iterable[T], closed: bool = True) -> Mapping[Tuple[T, ...], int]:
    safeseqs = iter2seq(iter2seq(seq) for seq in seqs)
    freqs = dict(matchingfrequencies(*safeseqs))

    res: Dict[Tuple[T, ...], Set[int]] = defaultdict(set)

    for k, seq in enumerate(safeseqs):
        for i, firstitem in enumerate(seq):
            freq = freqs[firstitem]

            p: Tuple[T, ...] = tuple()
            for j in range(i, len(seq)):
                item = seq[j]
                if freq != freqs[item]:
                    break

                p += (item,)

                res[p].add(k)

    results = {
        p: len(s) for p, s in res.items()
        if freqs[p[0]] == len(s)
    }

    if closed:
        for p in list(results.keys()):
            for q in enumeratesubseqs(p):
                results.pop(cast(Tuple[T, ...], q), None)

    return results


def partitionbysubseqs(subseqs: Iterable[Iterable[T]], seq: Iterable[T]) -> Iterable[Iterable[T]]:
    subseqs = set(iter2seq(seq) for seq in subseqs)
    seq = iter2seq(seq)

    lastj = 0
    i = 0
    while i < len(seq):
        j = i
        while j < len(seq):
            p = seq[i:j + 1]
            if tuple(p) in subseqs:
                if lastj < i:
                    yield seq[lastj:i]
                yield p
                lastj = j + 1

            j += 1

        i += 1

    if lastj < i:
        yield seq[lastj:i]


def templateseq(seqs: Iterable[Iterable[T]], default: Any = None, simple: bool = True) -> Iterable:
    safeseqs = iter2seq(iter2seq(seq) for seq in seqs)
    l = len(safeseqs)

    lastentries = [(i, -1) for i, _ in enumerate(safeseqs)]

    key = lambda p: sum(
        y - x
        for (_, x), (_, y) in zip(lastentries, p[1])
    )

    if simple:
        for k, entries in sorted(
                filter(
                    lambda p: len(p[1]) == l,
                    invertedindex(safeseqs).items()
                ),
                key=key
            ):
            conflict = False
            for (_, x), (_, y) in zip(lastentries, entries):
                if x + 1 > y:
                    conflict = True
                    break

                if x + 1 < y:
                    yield default
                    break

            if conflict:
                continue

            yield k
            lastentries = entries
    else:
        while True:
            k, entries = min(
                filter(
                    lambda p: len(p[1]) == l,
                    nextentries(safeseqs, lastentries).items()
                ),
                key=key,
                default=(None, None)
            )

            if k is None:
                break

            if any(
                    x + 1 < y
                    for (_, x), (_, y) in zip(lastentries, entries)
                ):
                yield default

            yield k
            lastentries = entries

    if any(
            x + 1 < len(seq)
            for (_, x), seq in zip(lastentries, safeseqs)
        ):
        yield default


def seq2grams(seq: Iterable[T], n: int, pad: Any = no_default) -> Iterable[Iterable[T]]:
    if pad is not no_default:
        seq = chain(repeat(pad, n - 1), seq, repeat(pad, n - 1))

    return sliding_window(n, seq)


def gramstats(seqs: Iterable[Iterable[T]], numgrams: int = 2) -> Mapping[Any, int]:
    c: Counter = Counter()
    for seq in seqs:
        c.update(seq2grams(seq, numgrams))

    return c


def probability(seq: Iterable[T], grams: Mapping[Any, int], numgrams: int = 2) -> float:
    total = sum(grams.values())

    prob = 0.0
    k = 0
    for gram in seq2grams(seq, numgrams):
        prob += math.log((grams.get(gram, 0) + 1) / total)
        k += 1

    return math.exp(prob / k)
