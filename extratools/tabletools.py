#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

def transpose(m: List[List[T]]) -> List[List[T]]:
    return [
        [r[i] for r in m]
        for i in range(len(m[0]))
    ]
