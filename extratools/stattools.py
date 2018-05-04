#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from statistics import median
from collections import Counter
from math import log2

from .rangetools import histogram # Alias

def medianabsdev(data: Iterable[float]) -> float:
    m = median(data)

    return median(abs(x - m) for x in data)


def entropy(data: Iterable[T]) -> float:
    counter = Counter(data)

    total = sum(counter.values())

    return -sum(
        p * log2(p)
        for p in (curr / total for curr in counter.values())
    )


def teststats(truths: Iterable[bool], predictions: Iterable[bool]) -> Tuple[int, int, int, int]:
    tp = fp = tn = fn = 0

    for truth, prediction in zip(truths, predictions):
        if prediction:
            if truth:
                tp += 1
            else:
                fp += 1
        else:
            if truth:
                fn += 1
            else:
                tn += 1

    return (tp, fp, tn, fn)


def precision(tp: int, fp: int, tn: int, fn: int) -> float:
    return tp / (tp + fp)


def recall(tp: int, fp: int, tn: int, fn: int) -> float:
    return tp / (tp + fn)


def f1(tp: int, fp: int, tn: int, fn: int, beta: float = 1) -> float:
    b = beta ** 2
    return (1 + b) * tp / ((1 + b) * tp + fp + b * fn)


def accuracy(tp: int, fp: int, tn: int, fn: int) -> float:
    return (tp + tn) / (tp + fp + tn + fn)
