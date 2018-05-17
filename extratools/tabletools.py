#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import csv
from io import TextIOBase
import regex as re

Table = Iterable[Union[List[T], Tuple[T]]]

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


def parse(lines: Iterable[str], sep=None) -> Table:
    for line in lines:
        yield line.split(sep)


def parsebyregex(lines: Iterable[str], regex: Any) -> Table:
    r = re.compile(regex) if isinstance(regex, str) else regex

    for line in lines:
        yield r.fullmatch(line).groups(default="")


def parsebyregexes(lines: Iterable[str], regexes: Any) -> Table:
    regexes = [
        re.compile(regex) if isinstance(regex, str) else regex
        for regex in regexes
    ]

    for line in lines:
        vals = [None] * len(regexes)

        start = 0
        for i, regex in enumerate(regexes):
            m = regex.search(line, start)
            vals[i] = m.group(0)
            start = m.end()

        yield vals
