[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/debugtools.py)

## Iterable

Tools for debugging iterable sequence.

### `delayediter`

`delayediter(seq, delay=None)` delays the production of each item in `seq` by `delay` seconds.

- In default, `delay=None` is disabled.

``` python
for v in delayediter(range(5), delay=1):
    print(datetime.datetime.now().time(), v)
# 01:11:21.562655 0
# 01:11:22.563725 1
# 01:11:23.567723 2
# 01:11:24.567997 3
# 01:11:25.568119 4
```

### `timediter`

`timediter(seq)` produces each item in `seq` and its respective timestamp when encountered.

``` python
for t, v in timediter(delayediter(range(5), delay=1)):
    print(datetime.datetime.fromtimestamp(t).time(), v)
# 01:13:37.181460 0
# 01:13:38.182715 1
# 01:13:39.188049 2
# 01:13:40.193304 3
# 01:13:41.197916 4
```

## System Diagnosis

Tools for non-functional but useful system diagnosis tools.

### `stopwatch`

`stopwatch()` returns both the duration since program start and the duration since last call in seconds.

!!! warning
    The stopwatch only starts after `debugtools` is imported.

### `peakmem`

`peakmem()` returns the peak memory usage since program start.

!!! danger
    In bytes on macOS, and in kilobytes on Linux.
