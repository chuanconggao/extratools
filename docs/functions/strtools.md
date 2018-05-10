[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

Tools for string matching.

- `commonsubstr(a, b)` finds the [longest common sub-string](https://en.wikipedia.org/wiki/Longest_common_substring_problem) among two strings `a` and `b`.

``` python
commonsubstr(
    "abbab",
    "aabbb"
)
# "abb"
```

- `editdist(a, b, bound=inf)` computes the [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between two strings `a` and `b`.

    - To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

``` python
editdist("dog", "frog")
# 2
```

- `tagstats(tags, lines, separator=None)` efficiently computes the number of lines containing each tag.

    - [TagStats](https://github.com/chuanconggao/TagStats) is used to compute efficiently, where the common prefixes among tags are matched only once.

    - `separator` is a regex to tokenize each string. In default when `separator` is `None`, each string is not tokenized.

``` python
tagstats(
    ["a b", "a c", "b c"],
    ["a b c", "b c d", "c d e"]
)
# {'a b': 1, 'a c': 0, 'b c': 2}
```

Tools for string transformations.

- `str2grams(s, n, pad=None)` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of string `s`.

    - Optional padding at the start and end can be added by specifying `pad`. `\0` is usually a safe choice for `pad` when not displaying.

Tools for checksums.

- `sha1sum(f)`, `sha256sum(f)`, `sha512sum(f)`, `md5sum(f)` compute the respective checksum, accepting string, bytes, text file object, and binary file object.

<a name="rangetools"></a>

