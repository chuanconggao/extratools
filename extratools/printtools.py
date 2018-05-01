#! /usr/bin/env python3

from functools import partial
import sys

print2 = partial(print, file=sys.stderr)
