[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/debugtools.py)

## Debugging

Tools for non-functional but useful debugging purposes.

### `stopwatch()`

Returns both the duration since program start and the duration since last call in seconds.

- Technically, the stopwatch starts when `debugtools` is imported.

### `peakmem()`

Returns the peak memory usage since program start.

- In bytes on macOS, and in kilobytes on Linux.
