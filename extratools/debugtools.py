#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import time
import resource

def delayediter(seq: Iterable[T], delay=None) -> Iterable[T]:
    for v in seq:
        if delay:
            time.sleep(delay)
        yield v


def timediter(seq: Iterable[T]) -> Iterable[Tuple[float, T]]:
    for v in seq:
        yield (time.time(), v)


starttime = lasttime = time.perf_counter()

def stopwatch() -> Tuple[float, float]:
    global lasttime

    now = time.perf_counter()
    result = (now - starttime, now - lasttime)
    lasttime = now

    return result


def peakmem() -> int:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
