#! /usr/bin/env python3

from typing import *

def __str2grams(s: str, n: int) -> Iterable[str]:
    yield from (
        s[i:i + n] for i in range(len(s) - n + 1)
    )


def str2grams(s: str, n: int, pad: str = None) -> Iterable[str]:
    if pad:
        if len(pad) > 1:
            raise ValueError

        pad = pad * (n - 1)

    if len(s) < n:
        if pad:
            yield from __str2grams(pad + s + pad, n)
        else:
            yield s
    else:
        if pad:
            yield from __str2grams(pad + s[:n - 1], n)

        yield from __str2grams(s, n)

        if pad:
            yield from __str2grams(s[-(n - 1):] + pad, n)
