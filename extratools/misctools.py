#! /usr/bin/env python3

from typing import *

def cmp(a: Any, b: Any) -> int:
    return (a > b) - (a < b)


def parsebool(s: str) -> bool:
    return s.strip().lower() in {
        "1", "+",
        "true", "yes", "positive",
        "真", "是", "正"
    }
