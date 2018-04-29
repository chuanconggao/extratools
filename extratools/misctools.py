#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

def cmp(a: T, b: T) -> int:
    return (a > b) - (a < b)
