# Problem 3108
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.val = [4294967296 - 1] * n

    def find(self, i: int):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int, w: int):
        irep = self.find(i)
        jrep = self.find(j)
        # Tweak the union find and process even if it is known that
        # both i and j are in the same set
        isize = self.size[irep]
        jsize = self.size[jrep]
        if isize < jsize:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]

        temp = self.val[jrep] & self.val[irep] & w
        self.val[jrep] = self.val[irep] = temp


class MinCostWalkInWeightedGraph:

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        uf = UnionFind(n)
        for [s, e, w] in edges:
            uf.union(s, e, w)

        res = []
        for [q1, q2] in query:
            f1 = uf.find(q1)
            f2 = uf.find(q2)

            res.append(-1 if f1 != f2 else uf.val[f1])

        return res


if __name__ == '__main__':
    m = MinCostWalkInWeightedGraph()
    print(m.minimumCost(3, [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], [[1, 2]]))
    print(m.minimumCost(5, [[0, 1, 7], [1, 3, 7], [1, 2, 1]], [[0, 3], [3, 4]]))
