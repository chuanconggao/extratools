[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

!!! success
    If not explicitly noted, a sequence refers to not only list, tuple, string, or [array](https://docs.python.org/3/library/array.html), but any iterable.

    If not explicitly noted, a function is lazy, where each sequence is processed incrmentally only when necessary and returned incrmentally as a generator.

!!! info
    Empty sequence is always a sub-sequence of any other sequence.

    A sequence is always a sub-sequence of itself.

!!! warning
    For tools related to specific tasks, please go to the respective documentation:

    - [Sub-sequence without gap](seqtools/seqwithoutgap).

    - [Sub-sequence with gap](seqtools/seqwithgap).

    - [Sequence encoding/decoding](seqtools/encode).

## Sequence Basics

Tools for basic sequence usages.

### `productcmp`

`productcmp(x, y)` compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

- Throw exception if `x` and `y` have different lengths.

``` python
productcmp(
    [1, 2, 3],
    [4, 5, 6]
)
# 1

productcmp(
    [1, 2, 3],
    [4, 3, 2]
)
# None
```

### `iter2seq`

`iter2seq(iterable, target=tuple)` converts any iterable sequence `iterable` to an indexable and sizable sequence with type `target=tuple` if necessary, defaults to tuple.

!!! warning
    This function reads the sequence at once.

!!! tip
    Useful if you need to scan the sequence more than once.

## Sequence Transformation

Tools for transforming sequence.

### `takeat`

`takeat(poss, seq)` takes the elements of `seq` at the positions in `poss`.

!!! danger
    `poss` must already be sorted.

!!! info
    Let $m$ be the length of `poss` and $n$ be the length of `seq`. The complexity of this function is $O(n)$.

!!! tip
    If `seq` supports random access, it is more efficient to use `[seq[i] for i in poss]`, with the complexity of $O(m)$.

``` python
list(takeat(range(0, 10, 3), range(100, 110)))
# [100, 103, 106, 109]
```

### `mergeseqs`

`mergeseqs(seqs, default=None, key=None)` merges the sequences of equal length in `seqs` into a single sequences. Returns `None` if there is conflict in any position.

- A position has conflict if there are more than one valid values, where each valid value is not `None` in default or judged by a key function `key`.

- `default` is a placeholder when there are no valid value in one position.

``` python
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

### `sortedbyrank`

`sortedbyrank(data, ranks, reverse=False)` returns the sorted list of `data`, according to the respective rank of each individual element in `ranks`.

``` python
sortedbyrank(
    ['a', 'b', 'c'],
    [  3,   2,   1]
)
# ['c', 'b', 'a']
```

### `filterbyother`

`filterbyother(func, seq)` drops the element in `seq` that fails the pairwise test `func` between the current element and any other element.

``` python
# Drop any number that is not the largest
list(filterbyother(lambda x, y: x >= y, [1, 2, 2, 3, 3, 3]))
# [3, 3, 3]

# Drop any set that is a superset of another set
list(filterbyother(
    lambda x, y: not x >= y,
    [{1,}, {1, 2}, {1, 2, 3}, {2, 3}, {2, 3, 4}]
))
# [{1}, {2, 3}]
```

## Sequence Alignment and Join

Tools for aligning and joining sequences.

### `matchingfrequencies`

`matchingfrequencies(*seqs, key=None)` returns each item and the respective number of sequences in `seqs` contains it.

- Optional key function `key` can be specified.

!!! tip
    If each sequence is sorted, then optimized [`sortedtools.matchingfrequencies`](sortedtools#matchingfrequencies) with the same API should be used for better efficiency.

    For the frequency of each item within a single sequence, use [`toolz.itertoolz.frequencies`](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.frequencies).

``` python
list(matchingfrequencies(
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2]
))
# [(0, 2), (1, 4), (2, 3), (3, 2), (4, 2)]
```

### `match`

`match(a, b, default=None)` matches two sequences `a` and `b` in pairs, such that the total number of matching pairs is maximized.

- If there are multiple alignments having the same number, the leftmost one is returned.

!!! warning
    This function reads all sequences at once.

!!! tip
    If both two sequences are sorted, respectively, then optimized [`sortedtools.sortedmatch`](sortedtools#sortedmatch) with the same API should be used for better efficiency.

``` python
list(match(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1]
))
# [(0, 0),
#  (None, 0),
#  (1, 1),
#  (1, 1),
#  (0, None),
#  (1, 1)]
```

### `align`

`align(a, b, cost=None, bound=inf, default=None)` computes the [alignment](https://en.wikipedia.org/wiki/Sequence_alignment) two sequences `a` and `b`, such that the total cost of the aligned sequences given the pair-wise cost function `cost(x, y)` is minimized.

- Assume the sequences after alignment are `a'` and `b'`. The total cost is `sum(cost(x, y) for x, y in zip(a', b'))`.

- Both the minimum total cost and the respective aligned sequences are returned as a tuple.

- In default, the cost function `cost(x, y)` returns `0` when `x == y` and `1` when not. This is equal to the [edit distance](https://en.wikipedia.org/wiki/Edit_distance).

- To speedup the computation, a threshold of maximum cost `bound=inf` can be specified. When there is no satisfying result, `None` is returned.

- If there are multiple alignments having the same cost, the leftmost one is returned.

!!! warning
    This function reads all sequences at once.

``` python
align(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1]
)
# (2, ([0, None, 1, 1,    0, 1],
#      [0,    0, 1, 1, None, 1]))

align(
    [0,    1, 1, 0, 1],
    [0, 0, 1, 1,    1],
    bound=1
)
# None
```

### `join`

`join(leftseq, rightseq, leftkey=None, rightkey=None, leftdefault=no_default, rightdefault=no_default)` joins two sequences, optionally according to `leftkey` and `rightkey`, respectively. Outer join is also supported.

!!! warning
    This function reads the first sequence `leftseq` at once. Thus, make `leftseq` the shorter one for best efficiency.

!!! tip
    If both two sequences are sorted according to `leftkey` and `rightkey`, respectively, then optimized [`sortedtools.sortedjoin`](sortedtools#sortedjoin) with the same API should be used for better efficiency.

!!! info
    `join` is just a wrapper of [`toolz.itertools.join`](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.join) with the same more friendly API of [`sortedtools.sortedjoin`](sortedtools#sortedjoin).

``` python
list(join(
    [   -1, -1, -2,    -4, -5,    -6],
    [0,  1,  1,  2, 3,  4,  5, 5],
    leftkey=abs, leftdefault=None
))
# [(None, 0),
#  (-1, 1),
#  (-1, 1),
#  (-1, 1),
#  (-1, 1),
#  (-2, 2),
#  (None, 3),
#  (-4, 4),
#  (-5, 5),
#  (-5, 5)]
```

### `cmpjoin`

`cmpjoin(leftseq, rightseq, func=operator.eq, leftdefault=no_default, rightdefault=no_default)` joins two sequences, optionally according to the condition function `func`, respectively. Outer join is also supported.

!!! warning
    This function reads the first sequence `leftseq` at once. Thus, make `leftseq` the shorter one for best efficiency.

!!! tip
    If both two sequences are sorted according to `leftkey` and `rightkey`, respectively, then optimized [`sortedtools.sortedjoin`](sortedtools#sortedjoin) with the same API should be used for better efficiency.

    This function is more flexable than [`join`](#join), and can be used in more scenarios.

``` python
list(cmpjoin(
    [   1, 1, 2,    4, 5,    -6],
    [0, 1, 1, 2, 3, 4, 5, 5]
))
# [(1, 1),
#  (1, 1),
#  (1, 1),
#  (1, 1),
#  (2, 2),
#  (4, 4),
#  (5, 5),
#  (5, 5)]

list(cmpjoin(
    [   1, 1, 2,    4, 5,    -6],
    [0, 1, 1, 2, 3, 4, 5, 5],
    lambda x, y: abs(x - y) == 1
))
# [(1, 0),
#  (1, 0),
#  (2, 1),
#  (2, 1),
#  (1, 2),
#  (1, 2),
#  (2, 3),
#  (4, 3),
#  (5, 4),
#  (4, 5),
#  (4, 5)]
```

### `templateseq`

`templateseq(seqs, default=None, simple=True)` finds the common template of all the sequences `seqs`. `default=None` is used to denote any placeholder sub-sequence.

- For better performance, option `simple` is enabled in default for only one scan of the sequences. However, it may work incorrectly for more complex template, which is:

    - Any part of the template appears more than once in the same sequence,
    
    - Any part of the template does not always appear before or after than another according to the same order part among sequences.

!!! warning
    This function reads all the sequences at once.

    This function reads all the sequences more than once when `simple = False`.

    Unlike `seqtools.commonsubseq(a, b)`, which finds the [longest common sub-sequence](https://en.wikipedia.org/wiki/Longest_common_substring_problem), this function does not guarantee finding the longest template.

!!! tip
    Essentially, each template is a closed sequential pattern covering all the sequences. Please check [PrefixSpan-py](https://github.com/chuanconggao/PrefixSpan-py) for more advanced scenarios.

``` python
list(templateseq((
    s.split() for s in [
        "Alice likes tea and coffee !",
        "Bob likes sushi and ramen !",
        "Elisa or Anna likes icecream and cake and cookie !"
    ]
), default='*'))
# ['*', 'likes', '*', 'and', '*', '!']

list(templateseq((
    s.split() for s in [
        "Alice likes tea and coffee !",
        "Bob likes sushi and ramen !",
        "Elisa or Anna likes icecream and cake and cookie !"
    ]
), default='*', simple=False))
# ['*', 'likes', '*', 'and', '*', '!']

# For more complex data.
list(templateseq((
    s.split() for s in [
        "! Alice likes tea and coffee ! !",
        "Bob likes sushi and ramen ! !",
        "Elisa or Anna likes icecream and cake and cookie ! !"
    ]
), default='*'))
# Incorrect template.
# ['*', 'likes', '*', 'and', '*']

list(templateseq((
    s.split() for s in [
        "! Alice likes tea and coffee ! !",
        "Bob likes sushi and ramen ! !",
        "Elisa or Anna likes icecream and cake and cookie ! !"
    ]
), default='*', simple=False))
# ['*', 'likes', '*', 'and', '*', '!', '!']
```

## Sequence Modeling

Tools for modeling sequences.

### `seq2grams`

`seq2grams(seq, n, pad=no_default)` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of sequence `seq`.

- Optional padding at the start and end can be added by specifying `pad`.

!!! tip
    For string, [`strtools.str2grams`](strtools#str2grams) can be used, which returns each gram as a string.

``` python
list(seq2grams(range(5), 3))
# [(0, 1, 2),
#  (1, 2, 3),
#  (2, 3, 4)]

list(seq2grams(range(5), 3, pad=None))
# [(None, None, 0),
#  (None, 0, 1),
#  (0, 1, 2),
#  (1, 2, 3),
#  (2, 3, 4),
#  (3, 4, None),
#  (4, None, None)]
```

### `gramstats`

`gramstats(seqs, numgrams=2)` computes the frequency of each `n`-grams in sequences `seqs`.

- where `n` is specified by `numgrams`.

``` python
gramstats([
    "python",
    "python2",
    "python2.7",
    "python3",
    "python3.7"
])
# {('p', 'y'): 5,
#  ('y', 't'): 5,
#  ('t', 'h'): 5,
#  ('h', 'o'): 5,
#  ('o', 'n'): 5,
#  ('n', '2'): 2,
#  ('2', '.'): 1,
#  ('.', '7'): 2,
#  ('n', '3'): 2,
#  ('3', '.'): 1}
```

### `probability`

`probability(seq, grams, numgrams=2)` computes the probability of generating sequence `seq` by the `n`-grams and their respective frequencies in `grams`.

- where `n` is specified by `numgrams`.

!!! tip
    There are many publicily available pre-trained `n`-grams models on text.

``` python
gs = gramstats([
    "python",
    "python2",
    "python2.7",
    "python3",
    "python3.7"
])

probability("pypy", gs)
# 0.10005840148165537

probability("pypy3", gs)
# 0.07422696190252057

```
