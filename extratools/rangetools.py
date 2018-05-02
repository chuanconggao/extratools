#! /usr/bin/env python3

from typing import *

Range = Tuple[float, float]

from math import inf
from bisect import bisect

def histogram(thresholds: List[float], data: Iterable[float], leftmost: float = -inf) -> Mapping[float, int]:
    stats = [0] * (len(thresholds) + 1)

    for v in data:
        pos = bisect(thresholds, v)
        stats[pos] += 1

    return dict(zip([leftmost] + thresholds, stats))


def merge(covers: Iterable[Range]) -> Iterable[Range]:
    covered: List[Range] = []

    laststart = None
    lastend = -inf
    for localstart, localend in sorted(covers, key=lambda p: p[0]):
        if lastend < localend:
            if len(covered) == 0 or lastend < localstart:
                covered.append((localstart, localend))

                laststart = localstart
            else:
                covered[-1] = (laststart, localend)

            lastend = localend

    return covered


def gaps(covers: Iterable[Range], whole: Range = (-inf, inf)) -> Iterable[Range]:
    start, end = whole

    uncovered: List[Range] = []

    lastend = start
    for localstart, localend in merge(covers):
        localstart = max(start, localstart)
        localend = min(end, localend)

        if lastend < localstart:
            uncovered.append((lastend, localstart))

        lastend = localend

    if lastend == start:
        return [whole]

    if lastend < end:
        uncovered.append((lastend, end))

    return uncovered
