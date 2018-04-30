#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

def sorteddiff(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = lambda v: v
    ) -> Iterable[T]:
    sentinel = object()

    x, y = iter(a), iter(b)

    m: Union[T, object] = sentinel
    n: Union[T, object] = sentinel

    while True:
        m, n = next(x, sentinel), next(y, sentinel) if n is sentinel else n
        if n is sentinel:
            break

        if m is sentinel:
            raise ValueError

        if key(m) == key(n):
            n = sentinel
        else:
            yield m

    while m is not sentinel:
        yield m

        m = next(x, sentinel)
