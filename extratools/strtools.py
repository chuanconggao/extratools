#! /usr/bin/env python3

from typing import *

from hashlib import sha1, sha256, sha512, md5
from io import TextIOBase, BufferedIOBase
import math
import regex as re

import tagstats as tagmatches
from toolz.itertoolz import no_default

from .seqtools import commonsubseq, align, seq2grams
from .rangetools import intersect

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


def str2grams(s: str, n: int, pad: str = '') -> Iterable[str]:
    if pad != '' and len(pad) > 1:
        raise ValueError

    if pad == '':
        pad = no_default

    for seq in seq2grams(s, n, pad):
        yield ''.join(seq)


def rewrite(s: str, regex: Any, template: str) -> str:
    r = re.compile(regex) if isinstance(regex, str) else regex

    m = r.fullmatch(s)
    return template.format(*m.groups(), **m.groupdict())


def learnrewrite(src: str, dst: str, minlen: int = 3) -> Tuple[str, str]:
    def replace(target, poss, forregex):
        for k, i, j in sorted(poss, key=lambda p: p[1], reverse=True):
            target = "{}{}{}".format(
                target[:i],
                ("({})" if forregex else "{{{}}}").format(r".*" if forregex else k),
                target[j:]
            )

        return target


    xs: List[Tuple[int, int, int]] = []

    lastj = 0
    for i in range(len(src)):
        if i < lastj:
            continue

        currp = p = -1
        for j in range(i + 1, len(src)):
            s = src[i:j]

            p = dst.find(s)
            if p < 0:
                break

            currp = p
            lastj = j

        if currp >= 0 and lastj - i >= minlen:
            xs.append((i, currp, lastj - i))

    ys: List[Tuple[int, int, int]] = []
    for x, y, l in sorted(xs, key=lambda p: p[2], reverse=True):
        if any(
                intersect((y, y + l), (yy, yy + ll), allowempty=True) is not None
                for _, yy, ll in ys
            ):
            continue

        ys.append((x, y, l))

    ys = sorted(ys, key=lambda p: p[0])

    return (
        replace(src, (
            (k, x, x + l) for k, (x, _, l) in enumerate(ys)
        ), forregex=True),
        replace(dst, (
            (k, y, y + l) for k, (_, y, l) in enumerate(ys)
        ), forregex=False)
    )


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
