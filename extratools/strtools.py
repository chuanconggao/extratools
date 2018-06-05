#! /usr/bin/env python3

from typing import *

from hashlib import sha1, sha256, sha512, md5
from io import TextIOBase, BufferedIOBase
import math
import regex as re

import tagstats as tagmatches
from toolz.itertoolz import no_default

from .seqtools import commonsubseq, align, seq2grams, enumeratesubseqs
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


def rewrite(s: str, regex: Any, template: str, transformations: Optional[Mapping[Union[str, int], Callable[[str], str]]] = None) -> str:
    r = re.compile(regex) if isinstance(regex, str) else regex

    m = r.fullmatch(s)

    gs = m.groups()
    gd = m.groupdict()
    if transformations:
        gs = [
            transformations.get(i, lambda x: x)(v)
            for i, v in enumerate(gs)
        ]
        gd = {
            k: transformations.get(k, lambda x: x)(v)
            for k, v in gd.items()
        }

    return template.format(*gs, **gd)


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


def extract(s: str, entities: Iterable[str], useregex=False, ignorecase=True) -> Iterable[str]:
    for m in re.compile(
            r"\b(?:{})\b".format(r"|".join(
                e if useregex else re.escape(e).replace(' ', r"s+") for e in entities
            )),
            re.I if ignorecase else 0
        ).finditer(s):
        yield m.group(0)


def __findeqtagpairspans(
        s: str,
        tag: str,
        useregex: bool = False
    ) -> Iterable[Tuple[Tuple[int, int], ...]]:
    for match in re.finditer(r"(?P<__open>{})(?P<__content>.*?)(?P<__close>\1)".format(tag if useregex else re.escape(tag)), s):
        yield (match.span("__open"), match.span("__content"), match.span("__close"))


def __findtagpairspans(
        s: str,
        tag: str, closetag: Optional[str] = None,
        useregex: bool = False
    ) -> Iterable[Tuple[Tuple[int, int], ...]]:
    if closetag is None or tag == closetag:
        yield from __findeqtagpairspans(s, tag, useregex=useregex)
        return

    if not useregex:
        tag = re.escape(tag)
        closetag = re.escape(closetag)

    retags = re.compile(r"(?P<__open>{})|(?P<__close>{})".format(tag, closetag))

    startspans = []

    for match in retags.finditer(s):
        opengroup = match.group("__open")
        if opengroup:
            startspans.append(match.span())
            continue

        closegroup = match.group("__close")
        if closegroup and startspans:
            startspan = startspans.pop()
            endspan = match.span()

            yield (startspan, (startspan[1], endspan[0]), endspan)


def findtagpairspans(
        s: str,
        tag: str, closetag: Optional[str] = None,
        useregex: bool = False
    ) -> Iterable[Tuple[int, int]]:
    return (
        (startspan[0], endspan[1])
        for startspan, _, endspan in __findtagpairspans(s, tag, closetag, useregex=useregex)
    )


def findtagpair(
        s: str, pos: int,
        tag: str, closetag: Optional[str] = None,
        useregex: bool = False
    ) -> Optional[str]:
    for startpos, endpos in findtagpairspans(s, tag, closetag, useregex=useregex):
        if startpos <= pos < endpos:
            return s[startpos:endpos]

    return None


def findmatchingtag(
        s: str, pos: int,
        tag: str, closetag: Optional[str] = None,
        useregex: bool = False
    ) -> Optional[Tuple[int, int]]:
    for startspan, _, endspan in __findtagpairspans(s, tag, closetag, useregex=useregex):
        if startspan[0] <= pos < endspan[1]:
            if pos < startspan[1]:
                return endspan

            return startspan

    return None


def removetagpair(
        s: str, pos: int,
        tag: str, closetag: Optional[str] = None,
        useregex: bool = False,
        removecontent: bool = False
    ) -> str:
    for startspan, midspan, endspan in __findtagpairspans(s, tag, closetag, useregex=useregex):
        if startspan[0] <= pos < endspan[1]:
            return s[:startspan[0]] + ('' if removecontent else s[slice(*midspan)]) + s[endspan[1]:]

    return s


def addtagpair(
        s: str, pos: int,
        tag: str, closetag: Optional[str] = None,
        newtag: Optional[str] = None, newclosetag: Optional[str] = None,
        useregex: bool = False
    ) -> str:
    if newtag is None:
        newtag = tag
    if newclosetag is None:
        newclosetag = newtag if closetag is None else closetag

    for startpos, endpos in findtagpairspans(s, tag, closetag, useregex=useregex):
        if startpos <= pos < endpos:
            return s[:startpos] + newtag + s[startpos:endpos] + newclosetag + s[endpos:]

    return s


def changetagpair(
        s: str, pos: int,
        tag: str, closetag: Optional[str] = None,
        newtag: Optional[str] = None, newclosetag: Optional[str] = None,
        useregex: bool = False
    ) -> str:
    if newtag is None:
        newtag = tag
    if newclosetag is None:
        newclosetag = newtag if closetag is None else closetag

    for startspan, midspan, endspan in __findtagpairspans(s, tag, closetag, useregex=useregex):
        if startspan[0] <= pos < endspan[1]:
            return s[:startspan[0]] + newtag + s[slice(*midspan)] + newclosetag + s[endspan[1]:]

    return s


def enumeratesubstrs(s: str) -> Iterable[str]:
    return map(str, enumeratesubseqs(s))


__renontext = re.compile(r"\W+", re.U)

def smartsplit(s: str) -> Tuple[Optional[str], Iterable[str]]:
    c: Counter = Counter()
    for sep in __renontext.findall(s):
        c.update([sep])
        c.update(set(enumeratesubstrs(sep)))

    if not c:
        return (None, [s])

    bestsep = max(
        c.items(),
        key=lambda p: (p[1], len(p[0]))
    )[0]

    return (bestsep, s.split(bestsep))


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
