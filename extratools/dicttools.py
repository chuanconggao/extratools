#! /usr/bin/env python3

from typing import *

KT = TypeVar("KT")
VT = TypeVar("VT")

T = TypeVar("T")

import collections
from collections import defaultdict
from itertools import count

from toolz.dicttoolz import merge

from . import jsontools

def invert(d: Mapping[KT, VT]) -> Mapping[VT, KT]:
    return {v: k for k, v in d.items()}


def invert_multiple(d: Mapping[KT, Union[VT, Iterable[VT]]]) -> Mapping[VT, KT]:
    return merge(
        {v: k for v in vs} if isinstance(vs, collections.Iterable) else {vs: k}
        for k, vs in d.items()
    )


def invert_safe(d: Mapping[KT, VT]) -> Mapping[VT, Iterable[KT]]:
    r: Mapping[VT, List[KT]] = defaultdict(list)

    for k, v in d.items():
        r[v].append(k)

    return r


def remap(data: Iterable[KT], mapping: Dict[KT, VT], key: Callable[[KT], VT] = None) -> Iterable[VT]:
    if key is None:
        c = count(start=0)
        key = cast(Callable[[KT], VT], lambda k: next(c))

    for k in data:
        yield mapping.setdefault(k, key(k))


Entries = List[Tuple[int, int]]

def invertedindex(seqs: Iterable[Sequence[T]], entries: Entries = None) -> Mapping[T, Entries]:
    index: Mapping[T, Entries] = defaultdict(list)

    for k, seq in enumerate(seqs):
        i, lastpos = entries[k] if entries else (k, -1)

        for p, item in enumerate(seq, start=(lastpos + 1)):
            l = index[item]
            if len(l) and l[-1][0] == i:
                continue

            l.append((i, p))

    return index


def nextentries(data: Sequence[Sequence[T]], entries: Entries) -> Mapping[T, Entries]:
    return invertedindex(
        (data[i][lastpos + 1:] for i, lastpos in entries),
        entries
    )


def flatten(d: Any, force: bool = False) -> Any:
    return jsontools.__flatten(d, force=force, json=False)
