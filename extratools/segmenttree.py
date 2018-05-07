#! /usr/bin/env python3

class SegmentTreeNode(object):
    def __init__(self, nodeRange, default=None):
        self.nodeRange = nodeRange
        self.value = default
        self.children = []
        self.parent = None


class SegmentTree(object):
    def __init__(self, keys, func=min, default=None, maxChildNum=2):
        self.func = func

        l = [
            SegmentTreeNode((k, k), default)
            for k in sorted(keys)
        ]
        self.mapping = {n.nodeRange[0]: n for n in l}

        while len(l) > 1:
            nl = []

            for i in range(0, len(l), maxChildNum):
                c = l[i:i + maxChildNum]
                n = SegmentTreeNode(
                    (c[0].nodeRange[0], c[-1].nodeRange[1]),
                    default
                )
                n.children = c
                for x in c:
                    x.parent = n

                nl.append(n)

            l = nl

        self.root = l[0]


    def update(self, keyValueDict):
        ul = set()

        for (k, v) in keyValueDict.items():
            node = self.mapping[k]

            if node.value != v:
                node.value = v
                if node.parent != None:
                    ul.add(node.parent)

        while len(ul) > 0:
            newUL = set()

            for node in ul:
                pv = self.func(x.value for x in node.children)
                if pv != node.value:
                    node.value = pv
                    if node.parent != None:
                        newUL.add(node.parent)

            ul = newUL


    def query(self, queryRange):
        def covers(b):
            return queryRange[0] <= b[0] and b[1] < queryRange[1]


        def intersects(b):
            return not (queryRange[1] <= b[0] or queryRange[0] > b[1])


        def query_aux(node):
            if covers(node.nodeRange):
                return node.value

            return self.func(
                query_aux(cNode)
                for cNode in node.children
                if intersects(cNode.nodeRange)
            )


        if queryRange[0] >= queryRange[1] or not intersects(self.root.nodeRange):
            return None

        return query_aux(self.root)
