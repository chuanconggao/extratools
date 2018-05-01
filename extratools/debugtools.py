#! /usr/bin/env python3

from typing import *

import time
import resource

starttime = lasttime = time.perf_counter()

def stopwatch() -> Tuple[float, float]:
    global lasttime

    now = time.perf_counter()
    result = (now - starttime, now - lasttime)
    lasttime = now

    return result


def peakmem() -> int:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
