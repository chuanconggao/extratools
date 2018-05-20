[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/mathtools.py)

Tools for math.

### `safediv`

`safediv(a, b)` avoids the `division by zero` exception, by returning infinite with proper sign.

!!! info
    Closely referring [IEEE Standard 754](https://en.wikipedia.org/wiki/IEEE_754).

``` python
safediv(0, 0)
# nan

safediv(1, 0)
# inf

safediv(-1, 0)
# -inf

safediv(1, 1)
# 1.0
```

### `product`

`product(*nums)` computes the product of all the numbers in `nums`.

``` python
product(*(0.1 * n for n in range(1, 101)))
# 9.332621544394479e+57
```
