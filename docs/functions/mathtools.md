[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/mathtools.py)

Tools for math.

- `safediv(a, b)` avoids the `division by zero` exception, by returning infinite with proper sign.

    - Closely referring [IEEE Standard 754](https://en.wikipedia.org/wiki/IEEE_754).
