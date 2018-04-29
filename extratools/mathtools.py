#! /usr/bin/env python3

from math import inf

def safediv(a: float, b: float) -> float:
    return inf * a if b == 0 else a / b
