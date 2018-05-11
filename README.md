[![PyPI version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

Extra functional tools that go beyond standard library's `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz), [`fancy`](https://github.com/Suor/funcy), and [`more-itertools`](https://github.com/erikrose/more-itertools).

- Like `toolz` and others, most of the tools are designed to be efficient, pure, and lazy. Several useful yet non-functional tools are also included.

- While `toolz` and others target basic scenarios, most tools in this library target more advanced and complete scenarios.

- A few useful CLI tools for respective functions are also installed. They are available as `extratools-[funcname]`.

Full documentation available [here](https://www.chuancong.site/extratools/).

## Plans

This library is under active development, and new functions are added on regular basis.

- Any idea or contribution is highly welcome.

- Currently adopted by [TopSim](https://github.com/chuanconggao/TopSim) and [PrefixSpan-py](https://github.com/chuanconggao/PrefixSpan-py).

Besides other interesting ideas, I am planning to make the following updates in recent days/weeks/months.

- Add `dicttools.unflatten` and `jsontools.unflatten`.

- Update `seqtools.commonsubseq`, `seqtools.commonsubseqwithgap`, `seqtools.align`, and `strtools.commonsubstr` to support more than two sequences/strings.

- Add `trie` and `suffixtree` (according to [generalized suffix tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree)).

## Index of Available Tools

- Functions:

[`seqtools`](https://chuanconggao.github.io/extratools/functions/seqtools)
[`sortedtools`](https://chuanconggao.github.io/extratools/functions/sortedtools)
[`strtools`](https://chuanconggao.github.io/extratools/functions/strtools)
[`rangetools`](https://chuanconggao.github.io/extratools/functions/rangetools)
[`dicttools`](https://chuanconggao.github.io/extratools/functions/dicttools)
[`jsontools`](https://chuanconggao.github.io/extratools/functions/jsontools)
[`settools`](https://chuanconggao.github.io/extratools/functions/settools)
[`tabletools`](https://chuanconggao.github.io/extratools/functions/tabletools)
[`mathtools`](https://chuanconggao.github.io/extratools/functions/mathtools)
[`stattools`](https://chuanconggao.github.io/extratools/functions/stattools)
[`misctools`](https://chuanconggao.github.io/extratools/functions/misctools)
[`printtools`](https://chuanconggao.github.io/extratools/functions/printtools)
[`debugtools`](https://chuanconggao.github.io/extratools/functions/debugtools)

- Data Structures:

[`disjointsets`](https://chuanconggao.github.io/extratools/datastructures/disjointsets)
[`defaultlist`](https://chuanconggao.github.io/extratools/datastructures/defaultlist)

- CLI Tools:

[`dicttools.remap`](https://chuanconggao.github.io/extratools/cli)
[`jsontools.flatten`](https://chuanconggao.github.io/extratools/cli)
[`jsontools.teststats`](https://chuanconggao.github.io/extratools/cli)

## Examples

Here are three examples out of dozens of our tools.

- `seqtools.compress(data, key=None)` compresses the sequence by encoding continuous identical `Item` to `(Item, Count)`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

- `rangetools.gaps(covered, whole=(-inf, inf))` computes the uncovered ranges of the whole range `whole`, given the covered ranges `covered`.

``` python
list(gaps(
    [(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)],
    (0, 1)
))
# [(0, 0.1), (0.2, 0.5), (0.9, 1)]
```

- `jsontools.flatten(data, force=False)` flattens a JSON object by returning `(Path, Value`) tuples with each path `Path` from root to each value `Value`.

``` python
flatten(json.loads("""{
  "name": "John",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
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

## Installation

This package is available on PyPI. Just use `pip3 install -U extratools` to install it.

## Other Libraries

The following libraries are highly recommended to use together with `extratools`.

[`toolz`](https://github.com/pytoolz/toolz)
[`sortedcontainers`](http://www.grantjenks.com/docs/sortedcontainers/index.html)
