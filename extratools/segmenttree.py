#! /usr/bin/env python3

from toolz.itertoolz import partition_all

class SegmentTreeNode(object):
    def __init__(self, keyrange, default=None):
        self.keyrange = keyrange
        self.value = default
        self.children = []
        self.parent = None


class SegmentTree(object):
    def __init__(self, keys, func=min, default=None, numchild=2):
        self.func = func

        l = [
            SegmentTreeNode((k, k), default)
            for k in sorted(keys)
        ]
        self.mapping = {n.keyrange[0]: n for n in l}

        while len(l) > 1:
            nl = []

            for c in partition_all(numchild, l):
                n = SegmentTreeNode(
                    (c[0].keyrange[0], c[-1].keyrange[1]),
                    default=default
                )
                n.children = c
                for x in c:
                    x.parent = n

                nl.append(n)

            l = nl

        self.root = l[0]


    def update(self, keyvals):
        ul = set()

        for k, v in keyvals.items():
            node = self.mapping[k]

            if node.value != v:
                node.value = v
                if node.parent != None:
                    ul.add(node.parent)

        while ul:
            newUL = set()

            for node in ul:
                pv = self.func(x.value for x in node.children)
                if pv != node.value:
                    node.value = pv
                    if node.parent != None:
                        newUL.add(node.parent)

            ul = newUL


    def query(self, queryrange):
        def covers(b):
            return queryrange[0] <= b[0] and b[1] < queryrange[1]


        def intersects(b):
            return not (queryrange[1] <= b[0] or queryrange[0] > b[1])


        def query_aux(node):
            if covers(node.keyrange):
                return node.value

            return self.func(
                query_aux(cNode)
                for cNode in node.children
                if intersects(cNode.keyrange)
            )


        if not intersects(self.root.keyrange):
            return None

        return query_aux(self.root)
