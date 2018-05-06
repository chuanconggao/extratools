#! /usr/bin/env python3

from typing import *

def cmp(a: Any, b: Any) -> int:
    """
    Restores the useful `cmp` function previously in Python 2.

    - Implemented according to [What's New in Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons).

    Args:
        a: An object.
        b: An object.

    Returns:
        An integer of -1, 0, or 1, denoteing whether a > b, a == b, or a < b, respectively.
    """

    return (a > b) - (a < b)


def parsebool(s: str) -> bool:
    """
    Parses a string to boolean.

    Args:
        s: A string.

    Returns:
        Whether the string contains certain keywords denoting positive.
    """

    return s.strip().lower() in {
        "1", "+",
        "true", "yes", "positive",
        "真", "是", "正"
    }
