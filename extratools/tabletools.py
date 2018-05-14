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


def mergecols(cols: Table, default=None) -> Optional[List[T]]:
    mergedcol = []

    for vals in zip(*cols):
        mergedvals = [
            val for val in vals
            if val is not None and val != ""
        ]
        if len(mergedvals) > 1:
            return None

        mergedcol.append(mergedvals[0] if mergedvals else default)

    return mergedcol
