#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from array import array

def iter2seq(a: Iterable[T], target=tuple) -> Sequence[T]:
    if isinstance(a, (list, str, tuple, array)):
        return a

    return target(a)
