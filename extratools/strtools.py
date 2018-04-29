#! /usr/bin/env python3

from typing import *

def str2grams(s: str, n: int) -> List[str]:
    return [
        s[i:i + n] for i in range(len(s) - n + 1)
    ] if len(s) >= n else [s]
