#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

Range = Tuple[float, float]

from math import inf
from bisect import bisect

from sortedcontainers import SortedListWithKey

from .segmenttree import SegmentTree

def histogram(thresholds: List[float], data: Iterable[float], leftmost: float = -inf) -> Mapping[float, int]:
    stats = [0] * (len(thresholds) + 1)

    for v in data:
        pos = bisect(thresholds, v)
        stats[pos] += 1

    return dict(zip([leftmost] + thresholds, stats))


def rangequery(keyvalues: Dict[float, T], query: Range, func: Callable[[Iterable[T]], T] = min) -> T:
    s = SegmentTree(keyvalues.keys(), func=func)
    s.update(keyvalues)
    return s.query(query)


def intersect(a: Range, b: Range, allowempty: bool = False) -> Optional[Range]:
    a1, a2 = a
    b1, b2 = b
    c1, c2 = max(a1, b1), min(a2, b2)

    return None if (c1 > c2 if allowempty else c1 >= c2) else (c1, c2)


def union(a: Range, b: Range) -> Optional[Range]:
    a1, a2 = a
    b1, b2 = b
    c1, c2 = min(a1, b1), max(a2, b2)

    return (c1, c2) if intersect(a, b) else None


def rangecover(whole: Range, covered: Iterable[Range]) -> Iterable[Range]:
    remainings = [whole]
    covered = set(covered)

    selected = SortedListWithKey(key=lambda x: x[0])

    while len(remainings) and len(covered):
        bestval, best = 0.0, None
        for curr in covered:
            currval = 0.0
            for gap in remainings:
                cover = intersect(gap, curr)
                if cover:
                    currval += cover[1] - cover[0]

            if currval > bestval:
                bestval, best = currval, curr

        if not best:
            return

        yield best

        selected.add(best)
        covered.remove(best)

        remainings = list(gaps(selected, whole))


def covers(covered: Iterable[Range]) -> Iterable[Range]:
    laststart = lastend = -inf
    for localstart, localend in covered:
        if lastend < localstart:
            if laststart < lastend:
                yield (laststart, lastend)

            laststart = localstart

        if lastend < localend:
            lastend = localend

    if laststart < lastend:
        yield (laststart, lastend)


def gaps(covered: Iterable[Range], whole: Range = (-inf, inf)) -> Iterable[Range]:
    start, end = whole

    lastend = start
    for localstart, localend in covered:
        localstart = max(start, localstart)
        localend = min(end, localend)

        if lastend < localstart:
            yield (lastend, localstart)

        if lastend < localend:
            lastend = localend

    if lastend < end:
        yield (lastend, end)
