[![PyPI version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

**Featured on GitHub's Trending Python repos on May 25, 2018. Thank you so much for support!**

145+ extra higher-level functional tools that go beyond standard library's `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz), [`funcy`](https://github.com/Suor/funcy), and [`more-itertools`](https://github.com/erikrose/more-itertools).

- Like `toolz` and others, most of the tools are designed to be efficient, pure, and lazy. Several useful yet non-functional tools are also included.

- While `toolz` and others target basic scenarios, this library targets more advanced and higher-level scenarios.

- A few useful CLI tools for respective functions are also installed. They are available as `extratools-[func]`.

**Full documentation is available [here](https://www.chuancong.site/extratools/).**

## Why this library?

Typical pseudocode has less than 20 lines, where each line is a higher-level description. However, when implementing, many lower-level details have to be filled in.

This library reduces the burden of writing and refining the lower-level details again and again, by including an extensive set of carefully designed general purpose higher-level tools.

## Current status and future plans?

There are currently 140+ functions among 17 categories, 3 data structures, and 3 CLI tools.

- Currently adopted by [TopSim](https://github.com/chuanconggao/TopSim) and [PrefixSpan-py](https://github.com/chuanconggao/PrefixSpan-py).

This library is under active development, and new tools are added on weekly basis.

- Any idea or contribution is highly welcome.

Besides many other interesting ideas, I am planning to make the following updates in recent days/weeks/months.

- Add `dicttools.unflatten` and `jsontools.unflatten`.

- Add `trie` and `suffixtree` (according to [generalized suffix tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree)).

- Update `seqtools.align` to support more than two sequences.

No plan to implement tools that are well covered by other popular libraries.

## Which tools are available?

- Function Categories:
[`debugtools`](https://chuanconggao.github.io/extratools/functions/debugtools)
[`dicttools`](https://chuanconggao.github.io/extratools/functions/dicttools)
[`gittools`](https://chuanconggao.github.io/extratools/functions/gittools)
[`graphtools`](https://chuanconggao.github.io/extratools/functions/graphtools)
[`htmltools`](https://chuanconggao.github.io/extratools/functions/htmltools)
[`jsontools`](https://chuanconggao.github.io/extratools/functions/jsontools)
[`mathtools`](https://chuanconggao.github.io/extratools/functions/mathtools)
[`misctools`](https://chuanconggao.github.io/extratools/functions/misctools)
[`printtools`](https://chuanconggao.github.io/extratools/functions/printtools)
[`rangetools`](https://chuanconggao.github.io/extratools/functions/rangetools)
[`recttools`](https://chuanconggao.github.io/extratools/functions/recttools)
[`seqtools`](https://chuanconggao.github.io/extratools/functions/seqtools)
[`settools`](https://chuanconggao.github.io/extratools/functions/settools)
[`sortedtools`](https://chuanconggao.github.io/extratools/functions/sortedtools)
[`stattools`](https://chuanconggao.github.io/extratools/functions/stattools)
[`strtools`](https://chuanconggao.github.io/extratools/functions/strtools)
[`tabletools`](https://chuanconggao.github.io/extratools/functions/tabletools)

- Data Structures:
[`defaultlist`](https://chuanconggao.github.io/extratools/datastructures/defaultlist)
[`disjointsets`](https://chuanconggao.github.io/extratools/datastructures/disjointsets)
[`segmenttree`](https://chuanconggao.github.io/extratools/datastructures/segmenttree)

- CLI Tools:
[`dicttools.remap`](https://chuanconggao.github.io/extratools/cli)
[`jsontools.flatten`](https://chuanconggao.github.io/extratools/cli)
[`stattools.teststats`](https://chuanconggao.github.io/extratools/cli)

## Any example?

Here are ten examples out of our hundreds of tools.

- [`jsontools.flatten(data, force=False)`](https://chuanconggao.github.io/extratools/functions/jsontools#flatten) flattens a JSON object by returning all the tuples, each with a path and the respective value.

``` python
import json
from extratools.jsontools import flatten

flatten(json.loads("""{
  "name": "John",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}"""))
# {'name': 'John',
#  'address.streetAddress': '21 2nd Street',
#  'address.city': 'New York',
#  'phoneNumbers[0].type': 'home',
#  'phoneNumbers[0].number': '212 555-1234',
#  'phoneNumbers[1].type': 'office',
#  'phoneNumbers[1].number': '646 555-4567',
#  'children': [],
#  'spouse': None}
```

- [`rangetools.gaps(covered, whole=(-inf, inf))`](https://chuanconggao.github.io/extratools/functions/rangetools#gaps) computes the uncovered ranges of the whole range `whole`, given the covered ranges `covered`.

``` python
from math import inf
from extratools.rangetools import gaps

list(gaps(
    [(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)],
    (0, 1)
))
# [(0, 0.1), (0.2, 0.5), (0.9, 1)]
```

- [`recttools.heatmap(rect, rows, cols, points, usepos=False)`](https://chuanconggao.github.io/extratools/functions/recttools#heatmap) computes the heatmap within rectangle `rect` by a grid of `rows` rows and `cols` columns.

``` python
from extratools.recttools import heatmap

heatmap(
    ((1, 1), (3, 4)),
    3, 4,
    [(1.5, 1.25), (1.5, 1.75), (2.75, 2.75), (2.75, 3.5), (3.5, 2.5)]
)
# {1: 2, 7: 1, 11: 1, None: 1}

heatmap(
    ((1, 1), (3, 4)),
    3, 4,
    [(1.5, 1.25), (1.5, 1.75), (2.75, 2.75), (2.75, 3.5), (3.5, 2.5)],
    usepos=True
)
# {(0, 1): 2, (1, 3): 1, (2, 3): 1, None: 1}
```

- [`setcover(whole, covered, key=len)`](https://chuanconggao.github.io/extratools/functions/settools#setcover) solves the [set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem) by covering the universe set `whole` as best as possible, using a subset of the covering sets `covered`.

``` python
from extratools.settools import setcover

list(setcover(
    { 1, 2, 3,         4,         5},
    [{1, 2, 3}, {2, 3, 4}, {2, 4, 5}]
))
# [{1, 2, 3}, {2, 4, 5}]
```

- [`seqtools.compress(data, key=None)`](https://chuanconggao.github.io/extratools/functions/seqtools/encode#compress) compresses the sequence `data` by encoding continuous identical items to a tuple of item and count, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

``` python
from extratools.seqtools import compress

list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

- [`mergeseqs(seqs, default=None, key=None)`](https://chuanconggao.github.io/extratools/functions/seqtools#mergeseqs) merges the sequences of equal length in `seqs` into a single sequences. Returns `None` if there is conflict in any position.

``` python
from extratools.seqtools import mergeseqs

seqs = [
    (0   , 0   , None, 0   ),
    (None, 1   , 1   , None),
    (2   , None, None, None),
    (None, None, None, None)
]

list(mergeseqs(seqs[1:]))
# [2,
#  1,
#  1,
#  None]

list(mergeseqs(seqs))
# None
```

- [`strtools.smartsplit(s)`]((https://chuanconggao.github.io/extratools/functions/strtools#smartsplit)) finds the best delimiter to automatically split string `s`. Returns a tuple of delimiter and split substrings.

``` python
from extratools.strtools import smartsplit

smartsplit("abcde")
# (None,
#  ['abcde'])

smartsplit("a b c d e")
# (' ',
#  ['a', 'b', 'c', 'd', 'e'])

smartsplit("/usr/local/lib/")
# ('/',
#  ['', 'usr', 'local', 'lib', ''])

smartsplit("a ::b:: c :: d")
# ('::',
#  ['a ', 'b', ' c ', ' d'])

smartsplit("{1, 2, 3, 4, 5}")
# (', ',
#  ['{1', '2', '3', '4', '5}'])
```

- [`strtools.learnrewrite(src, dst, minlen=3)`](https://chuanconggao.github.io/extratools/functions/strtools#learnrewrite) learns the respective regular expression and template to rewrite `src` to `dst`.

``` python
from extratools.strtools import learnrewrite

learnrewrite(
    "Elisa likes Apple.",
    "Apple is Elisa's favorite."
)
# ('(.*) likes (.*).',
#  "{1} is {0}'s favorite.")
```

- [`tabletools.parsebymarkdown(text)`](https://chuanconggao.github.io/extratools/functions/tabletools#parsebymarkdown) parses a text of multiple lines to a table, according to [Markdown](https://github.github.com/gfm/#tables-extension-) format.


``` python
from extratools.tabletools import parsebymarkdown

list(parsebymarkdown("""
| foo | bar |
| --- | --- |
| baz | bim |
"""))
# [['foo', 'bar'],
#  ['baz', 'bim']]
```

- [`tabletools.hasheader(data)`](https://chuanconggao.github.io/extratools/functions/tabletools#hasheader) returns the confidence (between `0` and `1`) of whether the first row of the table `data` is header.

``` python
from extratools.tabletools import hasheader

t = [
    ['Los Angeles'  , '34°03′'   , '118°15′'  ],
    ['New York City', '40°42′46″', '74°00′21″'],
    ['Paris'        , '48°51′24″', '2°21′03″' ]
]

hasheader(t)
# 0.0

hasheader([
    ['City', 'Latitude', 'Longitude']
] + t)
# 0.6666666666666666

hasheader([
    ['C1', 'C2', 'C3']
] + t)
# 1.0
```

## How to install?

This package is available on PyPI. Just use `pip3 install -U extratools` to install it.

To enable all the features, please install extra dependencies by `pip3 install -U sh RegexOrder TagStats`.

## How to cite?

When using for research purpose, please cite this library as follows.

``` tex
@misc{extratools,
  author = {Chuancong Gao},
  title = {{extratools}},
  howpublished = "\url{https://github.com/chuanconggao/extratools}",
  year = {2018}
}
```

## Any recommended library?

There are several great libraries recommended to use together with `extratools`:
[`regex`](https://pypi.org/project/regex/) [`sortedcontainers`](http://www.grantjenks.com/docs/sortedcontainers/index.html) [`toolz`](https://github.com/pytoolz/toolz) [`sh`](https://amoffat.github.io/sh/index.html)
