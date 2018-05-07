#! /usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages"
]

source_suffix = [
    ".rst",
    ".md"
]

source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser",
}

master_doc = "index"
