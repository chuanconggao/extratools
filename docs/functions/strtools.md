[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

!!! info
    As each string is a sequence, tools in `seqtools` can also be applied here. `strtools` only contains tools that are unique to the concept of string.

## String Matching

Tools for string matching.

### `commonsubstr(a, b)`

Finds the [longest common sub-string](https://en.wikipedia.org/wiki/Longest_common_substring_problem) among two strings `a` and `b`.

``` python
commonsubstr(
     "abbab",
    "aabbb"
)
# "abb"
```

### `editdist(a, b, bound=inf)`

Computes the [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between two strings `a` and `b`.

- To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

``` python
editdist(
     "dog",
    "frog"
)
# 2
```

### `tagstats(tags, lines, separator=None)`

Efficiently computes the number of lines containing each tag.

- `separator` is a regex to tokenize each string. In default when `separator` is `None`, each string is not tokenized.

!!! info
    [TagStats](https://github.com/chuanconggao/TagStats) is used to compute efficiently, where the common prefixes among tags are matched only once.

``` python
tagstats(
    ["a b", "a c", "b c"],
    ["a b c", "b c d", "c d e"]
)
# {'a b': 1, 'a c': 0, 'b c': 2}
```

## String Transformation

Tools for string transformations.

### `str2grams(s, n, pad=None)`

Returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of string `s`.

- Optional padding at the start and end can be added by specifying `pad`.

!!! tip
    `\0` is usually a safe choice for `pad` when not displaying.

``` python
list(str2grams("str2grams", 2, pad='#'))
# ['#s', 'st', 'tr', 'r2', '2g', 'gr', 'ra', 'am', 'ms', 's#']
```

## Checksum

Tools for checksums.

### `sha1sum(f)` , `sha256sum(f)`, `sha512sum(f)`, and `md5sum(f)`

Compute the respective checksum, accepting string, bytes, text file object, and binary file object.

``` python
sha1sum("strtools")
# 'bb91c4c3457cd1442acda4c11b29b02748679409'
```
