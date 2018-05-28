#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

import csv
from io import TextIOBase
import itertools
from itertools import combinations, permutations
import regex as re
import collections

from regexorder import RegexOrder
from toolz.itertoolz import isdistinct

from .seqtools import iter2seq
from .settools import dropsupersets

Table = Iterable[Union[List[T], Tuple[T, ...]]]

def transpose(data: Table) -> Table:
    for col in zip(*data):
        yield tuple(col)


def loadcsv(path: Union[Iterable[str], str, TextIOBase], delimiter: str = ',') -> Table:
    if isinstance(path, collections.Iterable):
        f = path
    else:
        f = cast(TextIOBase, path if isinstance(path, TextIOBase) else open(path, 'r', newline=''))

    yield from csv.reader(f, delimiter=delimiter)


def dumpcsv(path: Union[str, TextIOBase], data: Table, delimiter: str = ',') -> None:
    f = cast(TextIOBase, path if isinstance(path, TextIOBase) else open(path, 'w', newline=''))

    writer = csv.writer(f, delimiter=delimiter)
    for row in data:
        writer.writerow(row)


def mergecols(cols: Table, default=None, blank=None) -> Optional[List[T]]:
    mergedcol = []

    for vals in zip(*cols):
        mergedvals = [
            val for val in vals
            if val is not None and str(val).strip(blank) != ""
        ]
        if len(mergedvals) > 1:
            return None

        mergedcol.append(mergedvals[0] if mergedvals else default)

    return mergedcol


def trim(table: Table, blank=None) -> Table:
    def isempty(v):
        return v is None or str(v).strip(blank) == ""

    table = iter2seq(table)

    nonemptyflags = [
        any(not isempty(v) for v in col)
        for col in transpose(table)
    ]

    for row in table:
        if all(isempty(v) for v in row):
            continue

        yield list(itertools.compress(row, nonemptyflags))


def parse(lines: Iterable[str], sep=None, useregex=False) -> Table:
    if useregex:
        r = re.compile(sep) if isinstance(sep, str) else sep

        for line in lines:
            yield r.split(line)
    else:
        for line in lines:
            yield line.split(sep)


def parsebymarkdown(text: str) -> Table:
    for row in trim(
            parse(
                filter(lambda line: line, text.split('\n')),
                sep=r"(?<!\\)\|",
                useregex=True
            ),
            blank=" \t-:"
        ):
        yield list(map(str.strip, row))


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


def inferschema(data: Table) -> Tuple[str, ...]:
    r = RegexOrder()

    return tuple(r.matchall(col).name for col in transpose(data))


def candidatekeys(data: Table, maxcols: int = 1) -> Iterable[Tuple[int, ...]]:
    data = iter2seq(data)
    cols = list(transpose(data))

    return map(tuple, dropsupersets(map(set, (
        localcolids
        for i in range(1, maxcols + 1)
        for localcolids in combinations(range(len(cols)), i)
        if isdistinct(transpose(cols[j] for j in localcolids))
    ))))


def foreignkeys(primarydata: Table, primarykey: Tuple[int, ...], foreigndata: Table) -> Iterable[Tuple[int, ...]]:
    pdata = iter2seq(primarydata)
    pvals = set(
        tuple(row[j] for j in primarykey)
        for row in pdata
    )

    fdata = iter2seq(foreigndata)
    fcols = list(transpose(fdata))

    return (
        localcolids
        for localcolids in permutations(range(len(fcols)), len(primarykey))
        if set(transpose(fcols[j] for j in localcolids)) <= pvals
    )
