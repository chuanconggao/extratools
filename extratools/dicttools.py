#! /usr/bin/env python3

from typing import *

KT = TypeVar("KT")
VT = TypeVar("VT")

T = TypeVar("T")

from collections import defaultdict
from itertools import count

from toolz.dicttoolz import merge

from . import jsontools

def invert(d: Mapping[KT, VT]) -> Mapping[VT, KT]:
    return {v: k for k, v in d.items()}


def invert_multiple(d: Mapping[KT, Iterable[VT]]) -> Mapping[VT, KT]:
    return merge(
        {v: k for v in vs}
        for k, vs in d.items()
    )


def invert_safe(d: Mapping[KT, VT]) -> Mapping[VT, List[KT]]:
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


Index = Dict[T, List[Tuple[int, int]]]

def invertedindex(seqs: Iterable[Sequence[T]]) -> Index:
    index: Index = defaultdict(list)

    for i, seq in enumerate(seqs):
        for p, item in enumerate(seq):
            l = index[item]
            if len(l) and l[-1][0] == i:
                continue

            l.append((i, p))

    return index


def flatten(d: Any, force: bool = False) -> Any:
    return jsontools.__flatten(d, force=force, json=False)
