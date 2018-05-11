#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from functools import partial
from itertools import zip_longest
import sys
from io import StringIO

print2 = partial(print, file=sys.stderr)

def iter2str(seq: Iterable[T], limit=None) -> str:
    sentinel = object()

    i = iter(seq)

    s = StringIO()
    s.write('<')

    c = 0

    while True:
        v = next(i, sentinel)
        if v is sentinel:
            s.write('>')
            return s.getvalue()

        s.write(", {}".format(repr(v)) if c else repr(v))

        c += 1
        if limit and c >= limit:
            s.write(', ...>')
            return s.getvalue()


def alignment2str(*seqs: Iterable, default: Any = None) -> str:
    strs = []

    for i, col in enumerate(zip_longest(*seqs, fillvalue=default)):
        if i == 0:
            strs = [StringIO() for _ in col]
        else:
            for s in strs:
                s.write(' ')

        vals = ['' if v is default else repr(v) for v in col]
        maxlen = max(len(val) for val in vals)
        pads = [(maxlen - len(val)) * ' ' for val in vals]

        for s, pad, val in zip(strs, pads, vals):
            s.write(pad)
            s.write(val)

    return '\n'.join([s.getvalue() for s in strs])


def table2str(data: List[List], default: Any = None) -> str:
    return alignment2str(*data, default=default)
