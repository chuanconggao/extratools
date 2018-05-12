#! /usr/bin/env python3

from typing import *

from itertools import groupby, product

from toolz import itertoolz
from toolz.utils import no_default

def join(
        leftseq, rightseq,
        leftkey=None, rightkey=None,
        leftdefault=no_default, rightdefault=no_default
    ):
    if not leftkey:
        leftkey = lambda x: x
    if not rightkey:
        rightkey = lambda x: x

    return itertoolz.join(leftkey, leftseq, rightkey, rightseq, leftdefault, rightdefault)


def __sortedjoin(
        leftseq, rightseq,
        leftkey=None, rightkey=None,
        leftdefault=no_default, rightdefault=no_default
    ):
    if not leftkey:
        leftkey = lambda x: x
    if not rightkey:
        rightkey = lambda x: x

    sentinel = object()

    x, y = iter(groupby(leftseq, leftkey)), iter(groupby(rightseq, rightkey))

    m: Any = sentinel
    n: Any = sentinel

    while True:
        if m is sentinel:
            m = next(x, sentinel)
        if n is sentinel:
            n = next(y, sentinel)

        if m is sentinel or n is sentinel:
            break

        if leftkey(m[0]) < rightkey(n[0]):
            if rightdefault is not no_default:
                yield (m[1], [rightdefault])

            m = sentinel
        elif leftkey(m[0]) > rightkey(n[0]):
            if leftdefault is not no_default:
                yield ([leftdefault], n[1])

            n = sentinel
        else:
            yield (m[1], n[1])

            m = n = sentinel

    if rightdefault is not no_default:
        while m is not sentinel:
            yield (m[1], [rightdefault])

            m = next(x, sentinel)

    if leftdefault is not no_default:
        while n is not sentinel:
            yield ([leftdefault], n[1])

            n = next(y, sentinel)


def sortedjoin(
        leftseq, rightseq,
        leftkey=None, rightkey=None,
        leftdefault=no_default, rightdefault=no_default
    ):
    for m, n in __sortedjoin(
            leftseq, rightseq,
            leftkey=leftkey, rightkey=rightkey,
            leftdefault=leftdefault, rightdefault=rightdefault
        ):
        yield from product(m, n)
