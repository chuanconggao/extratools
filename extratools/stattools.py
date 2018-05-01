#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from statistics import median
from collections import Counter
from math import log2, inf
from bisect import bisect

def medianabsdev(data: Iterable[float]) -> float:
    m = median(data)

    return median(abs(x - m) for x in data)


def entropy(data: Iterable[T]) -> float:
    counter = Counter(data)

    total = sum(counter.values())

    return -sum(
        p * log2(p)
        for p in (curr / total for curr in counter.values())
    )


def histogram(thresholds: List[float], data: Iterable[float]) -> Mapping[float, int]:
    stats = [0] * (len(thresholds) + 1)

    for v in data:
        pos = bisect(thresholds, v)
        stats[pos] += 1

    return dict(zip([-inf] + thresholds, stats))
