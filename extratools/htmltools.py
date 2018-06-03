#! /usr/local/bin/python3

from typing import *

import os

import sh

from .printtools import print2

def emmet(abbr: str) -> Optional[str]:
    npmdir = os.path.join(os.path.dirname(__file__), "htmltools")

    if not os.path.isdir(os.path.join(npmdir, "node_modules")):
        print2("Installing Node.js dependencies...\n")
        sh.npm(
            "install", "@emmetio/expand-abbreviation",
            _cwd=npmdir
        )

    return sh.node(
        "emmet.js", abbr,
        _cwd=npmdir
    )
