#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import csv
from io import TextIOBase

Table = Iterable[List[T]]

def transpose(data: Table) -> Table:
    for col in zip(*data):
        yield list(col)


def loadcsv(path: Union[str, TextIOBase], delimiter: str = ',') -> Table:
    f = cast(TextIOBase, path if isinstance(path, TextIOBase) else open(path, 'r', newline=''))

    yield from csv.reader(f, delimiter=delimiter)


def dumpcsv(path: Union[str, TextIOBase], data: Table, delimiter: str = ',') -> None:
    f = cast(TextIOBase, path if isinstance(path, TextIOBase) else open(path, 'w', newline=''))

    writer = csv.writer(f, delimiter=delimiter)
    for row in data:
        writer.writerow(row)
