[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

!!! info
    Tools in [`seqtools`](seqtools) can also be applied here. `strtools` only contains tools that are unique to the concept of string.

## String Matching

Tools for string matching.

!!! info
    Commonly used [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) is available as [`settools.jaccard`](settools/similarity#jaccard).

### `commonsubstr`

`commonsubstr(a, b)` finds the [longest common sub-string](https://en.wikipedia.org/wiki/Longest_common_substring_problem) among two strings `a` and `b`.

``` python
commonsubstr(
     "abbab",
    "aabbb"
)
# "abb"
```

### `editdist`

`editdist(a, b, bound=inf)` computes the [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between two strings `a` and `b`.

- To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

``` python
editdist(
     "dog",
    "frog"
)
# 2
```

### `tagstats`

`tagstats(tags, lines, separator=None)` efficiently computes the number of lines containing each tag.

- `separator` is a regex to tokenize each string. In default when `separator` is `None`, each string is not tokenized.

!!! success
    [TagStats](https://github.com/chuanconggao/TagStats) is used to compute efficiently, where the common prefixes among tags are matched only once.

``` python
tagstats(
    ["a b", "a c", "b c"],
    ["a b c", "b c d", "c d e"]
)
# {'a b': 1, 'a c': 0, 'b c': 2}
```

### `extract`

`extract(s, entities, useregex=False, ignorecase=True)` extracts the entities defined in `entities` from string `s`.

- Regular expression can be used to define each entity by specifying `useregex = True`.

- `ignorecase=True` specifies whether to ignore case when matching.

!!! tip
    Compatible third party library [`regex`](https://pypi.org/project/regex/) is used instead of standard library `re`, to support advanced unicode features.

``` python
# From Python Documentation
s = """
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). 
However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode string with a byte pattern or vice-versa;
similarly, when asking for a substitution, the replacement string must be of the same type as both the pattern and the search string.
"""

set(extract(s, ["str", "byte", "unicode string", "pattern"]))
# {'pattern', 'byte', 'Unicode string', 'str'}

set(extract(s, ["str", "byte", "unicode strings?", "patterns?"], useregex=True))
# {'Unicode string', 'patterns', 'byte', 'Unicode strings', 'str', 'pattern'}
```

## String Transformation

Tools for string transformations.

### `smartsplit`

`smartsplit(s)` finds the best delimiter to automatically split string `s`. Returns a tuple of delimiter and split substrings.

!!! info
    The delimiter is the most frequent non-text substring, by the number of longest non-text substrings containing it.

!!! tip
    The behavior here is designed to be similar to [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split).

``` python
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

### `rewrite`

`rewrite(s, regex, template, transformations=None)` rewrites a string `s` according to the template `template`, where the values are extracted according to the regular expression `regex`.

- Optional parameter `transformations` specifies a dictionary to transform each value. In the dictionary, each key is a group ID and each value is a function.

!!! tip
    Check [`re`](https://docs.python.org/3/library/re.html) for details of naming capturing group.

    Check [`str.format`](https://docs.python.org/3.4/library/string.html#formatstrings) for details of referring captured values in template.

``` python
rewrite(
    "Elisa likes Apple.",
    r"(\w+) likes (\w+).",
    "{1} is {0}'s favorite."
)
# "Apple is Elisa's favorite."

rewrite(
    "Elisa likes Apple.",
    r"(?P<name>\w+) likes (?P<item>\w+).",
    "{item} is {name}'s favorite."
)
# "Apple is Elisa's favorite."

rewrite(
    "Elisa likes Apple.",
    r"(?P<name>\w+) likes (?P<item>\w+).",
    "{item} is {name}'s favorite.",
    {"item": str.upper}
)
# "APPLE is Elisa's favorite."
```

### `learnrewrite`

`learnrewrite(src, dst, minlen=3)` learns the respective regular expression and template to rewrite `src` to `dst`.

- Please check [`rewrite`](strtools#rewrite) for details of the regular expression and template.

- `minlen=3` specifies the minimum length for each substitution.

!!! warning
    As regular expression is greedy, it cannot learn capturing groups next to each other.

``` python
learnrewrite(
    "Elisa likes Apple.",
    "Apple is Elisa's favorite."
)
# ('(.*) likes (.*).',
#  "{1} is {0}'s favorite.")

rewrite(
    "Elisa likes Apple.",
    *learnrewrite(
        "Elisa likes Apple.",
        "Apple is Elisa's favorite."
    )
)
# "Apple is Elisa's favorite."
```

## Substring Enumeration

Tools for enumerating substrings.

### `enumeratesubstrs`

`enumeratesubstrs(s)` enumerates all of `seq`'s non-empty substrings in [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order).

- Although `s` is a substring of itself, it is not returned.

``` python
list(enumeratesubstrs("abcd"))
# ['a',
#  'ab',
#  'abc',
#  'b',
#  'bc',
#  'bcd',
#  'c',
#  'cd',
#  'd']
```

## String Modeling

Tools for modeling strings.

### `str2grams`

`str2grams(s, n, pad='')` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of string `s`.

- Optional padding at the start and end can be added by specifying `pad`.

!!! tip
    `\0` is usually a safe choice for `pad` when not displaying.

``` python
list(str2grams("str2grams", 2, pad='#'))
# ['#s', 'st', 'tr', 'r2', '2g', 'gr', 'ra', 'am', 'ms', 's#']
```

## Checksum

Tools for checksums.

### `sha1sum` , `sha256sum`, `sha512sum`, and `md5sum`

`sha1sum(f)` , `sha256sum(f)`, `sha512sum(f)`, and `md5sum(f)` compute the respective checksum, accepting string, bytes, text file object, and binary file object.

``` python
sha1sum("strtools")
# 'bb91c4c3457cd1442acda4c11b29b02748679409'
```
