#! /usr/bin/env python3

from typing import *

import re
from hashlib import sha1, sha256, sha512, md5
from io import TextIOBase, BufferedIOBase
import math

import tagstats as tagmatches

from .seqtools import commonsubseq, align

def commonsubstr(a: str, b: str) -> str:
    return ''.join(commonsubseq(list(a), list(b)))


def editdist(a: str, b: str, bound: float = math.inf) -> float:
    res = align(list(a), list(b), bound=bound)
    return res[0] if res else None


def tagstats(tags: Iterable[str], lines: Iterable[str], separator: str = None) -> Mapping[str, int]:
    tagmatches.tagstats.tokenizer = None if separator is None else re.compile(separator)

    return {
        tag: sum(matches)
        for tag, matches in tagmatches.compute(
            lines,
            {tag: [tag] for tag in tags}
        ).items()
    }


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


def __checksum(f: Any, func: Callable[[bytes], Any]) -> str:
    content: bytes

    if isinstance(f, str):
        content = f.encode("utf-8")
    elif isinstance(f, bytes):
        content = f
    elif isinstance(f, TextIOBase):
        content = f.read().encode("utf-8")
    elif isinstance(f, BufferedIOBase):
        content = f.read()

    return func(content).hexdigest()


def sha1sum(f: Any) -> str:
    return __checksum(f, sha1)


def sha256sum(f: Any) -> str:
    return __checksum(f, sha256)


def sha512sum(f: Any) -> str:
    return __checksum(f, sha512)


def md5sum(f: Any) -> str:
    return __checksum(f, md5)
