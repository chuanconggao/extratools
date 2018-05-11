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

        s.write(f", {v}" if c else f"{v}")

        c += 1
        if limit and c >= limit:
            s.write(', ...>')
            return s.getvalue()


def alignment2str(a: Iterable, b: Iterable, default: Any = None) -> str:
    astr = StringIO()
    bstr = StringIO()

    for i, (x, y) in enumerate(zip_longest(a, b, fillvalue=default)):
        if i > 0:
            astr.write(' ')
            bstr.write(' ')

        aval = '' if x is default else repr(x)
        bval = '' if y is default else repr(y)

        apadding = (len(bval) - len(aval)) * ' '
        bpadding = (len(aval) - len(bval)) * ' '

        astr.write(apadding)
        astr.write(aval)

        bstr.write(bpadding)
        bstr.write(bval)

    return '\n'.join([astr.getvalue(), bstr.getvalue()])
