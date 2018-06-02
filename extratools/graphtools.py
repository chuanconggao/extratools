#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from collections import Counter

from .seqtools import iter2seq

def approxpagerank(objs: Iterable[T], func: Callable[[T, T], float]) -> Iterable[float]:
    objs = iter2seq(objs)

    ranks: List[float] = [0] * len(objs)

    for i, obj in enumerate(objs):
        for j in range(i + 1, len(objs)):
            sim = func(obj, objs[j])
            if sim > 0:
                ranks[i] += sim
                ranks[j] += sim

    return ranks
