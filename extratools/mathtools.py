#! /usr/bin/env python3

from math import inf
from functools import reduce
import operator

def safediv(a: float, b: float) -> float:
    return inf * a if b == 0 else a / b


def product(*nums: float) -> float:
    return reduce(operator.mul, nums, 1)
