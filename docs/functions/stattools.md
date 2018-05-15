[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/stattools.py)

## Statistics

Tools for statistics.

### `medianabsdev`

`medianabsdev(data)` computes the [median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation) of a sequence of floats.

### `entropy`

`entropy(data)` computes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of a sequence of any items.

!!! tip
    You can also pass a dictionary of `(item, frequency)` as known frequency distribution as `data`.

## Binary Classification

Tools for binary classification.

### `teststats`

`teststats(truths, predictions)` matches the truth labels and the prediction labels. Return a tuples of `(tp, fp, tn, fn)` as [true positive, false positive, true negative, and false negative](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers).

### `accuracy`

`accuracy(tp, fp, tn, fn)` returns the [accuracy](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers).

!!! tip
    You can simply call `accuracy(*teststats(truths, predictions))`.

### `precision`, `recall`, and `f1`

`precision(tp, fp, tn, fn)` and `recall(tp, fp, tn, fn)` return the [precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall).

`f1(tp, fp, tn, fn, beta=1)` returns the [F$_1$ measure](https://en.wikipedia.org/wiki/F1_score) in default, and returns the F$_\beta$ measure when `beta` is specified.
