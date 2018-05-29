[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/debugtools.py)

## Iterable

Tools for debugging iterable.

### `delayediter`

`delayediter(iterable, delay=None)` delays the production of each item in iterable `iterable` by a delay of `delay` in seconds.

- In default, `delay=None` disables the delay.

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

`timediter(iterable)` produces each item in iterable `iterable` and its respective timestamp when encountered.

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

Non-Functional but useful tools for system diagnosis.

### `stopwatch`

`stopwatch()` returns both the duration since program start and the duration since last call of this function in seconds.

!!! warning
    The stopwatch starts only after `debugtools` is imported.

``` python
for i in range(5):
    print(stopwatch())
    sleep(1)
# (1.4512503190198913, 1.4512503190198913)
# (2.45514269702835  , 1.0038923780084588)
# (3.4569691279903054, 1.0018264309619553)
# (4.45844506600406  , 1.0014759380137548)
# (5.463522073987406 , 1.0050770079833455)
```

### `peakmem`

`peakmem()` returns the peak memory usage since program start.

!!! danger
    In bytes on macOS, and in kilobytes on Linux.
