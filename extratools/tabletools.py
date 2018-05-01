#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import csv
from io import TextIOBase

Table = List[List[T]]

def transpose(data: Table) -> Table:
    return [list(row) for row in zip(*data)]


def loadcsv(path: Union[str, TextIOBase]) -> Table:
    f = cast(TextIOBase, path if isinstance(path, TextIOBase) else open(path, 'w', newline=''))

    return list(csv.reader(f))


def dumpcsv(path: Union[str, TextIOBase], data: Table) -> None:
    f = cast(TextIOBase, path if isinstance(path, TextIOBase) else open(path, 'w', newline=''))

    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
