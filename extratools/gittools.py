#! /usr/local/bin/python3

from typing import *

import os

import sh

def status(path: str = '.') -> Optional[Mapping[str, Any]]:
    output = sh.git(
        "status", "-s", "-b", "--porcelain=2",
        _cwd=os.path.expanduser(path)
    )

    if output == "":
        return None

    head = None
    upstream = None

    ahead, behind = 0, 0

    modified: List[str] = []
    untracked: List[str] = []

    for line in output.rstrip('\n').splitlines():
        if line.startswith('#'):
            if line.startswith("# branch.oid "):
                oid = line.rsplit(' ', 1)[1]
            if line.startswith("# branch.head "):
                branch = line.rsplit(' ', 1)[1]
                if branch != "(detached)":
                    head = branch
            elif line.startswith("# branch.upstream "):
                branch = line.rsplit(' ', 1)[1]
                if branch != "(detached)":
                    upstream = branch
            elif line.startswith("# branch.ab "):
                ahead, behind = [abs(int(x)) for x in line.rsplit(' ', 2)[1:]]
        elif line.startswith('?'):
            untracked.append(line.rsplit(' ', -1)[1])
        elif not line.startswith('!'):
            vals = line.split(' ')

            s, _, _, u = vals[2]
            flag = s == 'S' and u == 'U'

            (untracked if flag else modified).append(vals[-1])

    return {
        "path": path,
        "oid": oid,
        "branch": {
            "head": head,
            "upstream": upstream
        },
        "commits": {
            "ahead": ahead,
            "behind": behind
        },
        "files": {
            "modified": modified,
            "untracked": untracked
        }
    }
