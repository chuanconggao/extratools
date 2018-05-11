#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from functools import partial
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

        s.write(f", {v}" if c else f"{v}")

        c += 1
        if limit and c >= limit:
            s.write(', ...>')
            return s.getvalue()
