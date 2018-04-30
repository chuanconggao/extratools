#! /usr/bin/env python3

from typing import *

from statistics import median

def medianabsdev(data: Iterable[float]) -> float:
    m = median(data)

    return median(abs(x - m) for x in data)
