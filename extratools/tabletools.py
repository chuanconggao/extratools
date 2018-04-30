#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

Table = List[List[T]]

def transpose(data: Table) -> Table:
    return [list(row) for row in zip(*data)]
