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
    There are many publicly available pre-trained `n`-grams models on text.

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

