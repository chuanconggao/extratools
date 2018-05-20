#! /usr/bin/env python3

from typing import *

Point = Tuple[float, float]
Rectangle = Tuple[Point, Point]

from enum import IntEnum

class PointCmp(IntEnum):
    EQUAL = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = -1
    TOP_LEFT = -2
    BOTTOM_RIGHT = 2


def pointcmp(point1: Point, point2: Point) -> Optional[int]:
    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 == y2:
        return PointCmp.EQUAL

    if x1 <= x2 and y1 <= y2:
        return PointCmp.TOP_RIGHT

    if x1 >= x2 and y1 >= y2:
        return PointCmp.BOTTOM_LEFT

    if x1 <= x2 and y1 >= y2:
        return PointCmp.BOTTOM_RIGHT

    return PointCmp.TOP_LEFT


def allpoints(rect: Rectangle) -> Tuple[Point, Point, Point, Point]:
    p, q = rect
    s = (q[0], p[1])
    t = (p[0], q[1])

    return (p, s, q, t)


def __isvalid(point1: Point, point2: Point) -> bool:
    return pointcmp(point1, point2) in {0, 1}


def size(rect: Rectangle) -> float:
    (x1, y1), (x2, y2) = rect

    return (x2 - x1) * (y2 - y1)


def issubrect(rect1: Rectangle, rect2: Rectangle) -> bool:
    return intersect(rect1, rect2) == rect1


def intersect(rect1: Rectangle, rect2: Rectangle) -> Optional[Rectangle]:
    p1, q1 = rect1
    p2, q2 = rect2

    a = max(p1[0], p2[0])
    b = max(p1[1], p2[1])
    c = min(q1[0], q2[0])
    d = min(q1[1], q2[1])

    p, q = (a, b), (c, d)

    return (p, q) if __isvalid(p, q) else None


def union(rect1: Rectangle, rect2: Rectangle, force: bool = False) -> Optional[Rectangle]:
    p1, q1 = rect1
    p2, q2 = rect2

    a = min(p1[0], p2[0])
    b = min(p1[1], p2[1])
    c = max(q1[0], q2[0])
    d = max(q1[1], q2[1])

    return ((a, b), (c, d)) if force or intersect(rect1, rect2) else None


def grid(rect: Rectangle, rows: int, cols: int) -> Iterable[Rectangle]:
    (x1, y1), (x2, y2) = rect
    ww = (x2 - x1) / cols
    hh = (y2 - y1) / rows

    for row in range(rows):
        for col in range(cols):
            x, y = x1 + col * ww, y1 + row * hh

            yield ((x, y), (x + ww, y + hh))


def locatebypos(rect: Rectangle, rows: int, cols: int, pos: Tuple[int, int]) -> Tuple[int, Rectangle]:
    (x1, y1), (x2, y2) = rect
    ww = (x2 - x1) / cols
    hh = (y2 - y1) / rows

    row, col = pos

    x, y = x1 + col * ww, y1 + row * hh

    return (
        col + row * cols,
        ((x, y), (x + ww, y + hh))
    )


def locatebyid(rect: Rectangle, rows: int, cols: int, rectid: int) -> Tuple[int, Rectangle]:
    return locatebypos(rect, rows, cols, divmod(rectid, cols))


def locatebypoint(rect: Rectangle, rows: int, cols: int, point: Point) -> Tuple[int, Rectangle]:
    (x1, y1), (x2, y2) = rect
    ww = (x2 - x1) / cols
    hh = (y2 - y1) / rows

    xx, yy = point

    col = int((xx - x1) // ww)
    row = int((yy - y1) // hh)

    return locatebypos(rect, rows, cols, (col, row))
