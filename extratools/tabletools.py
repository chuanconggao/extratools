#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import csv

Table = List[List[T]]

def transpose(data: Table) -> Table:
    return [list(row) for row in zip(*data)]


def loadcsv(path: str) -> Table:
    with open(path, newline='') as f:
        return list(csv.reader(f))


def dumpcsv(path: str, data: Table) -> None:
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
