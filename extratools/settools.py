#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

def addtoset(s: Set[T], x: T) -> bool:
    if x in s:
        return False

    s.add(x)
    return True
