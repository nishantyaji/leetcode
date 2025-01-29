# Problem 684
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i: int):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return

        isize = self.size[irep]
        jsize = self.size[jrep]
        if isize < jsize:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]


class RedundantConnection:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited, res = set(), [-1, -1]
        nodes = set()
        for s, e in edges:
            nodes.add(s)
            nodes.add(e)
        uf = UnionFind(len(nodes))
        for s, e in edges:
            if s in visited and e in visited and uf.find(s - 1) == uf.find(e - 1):
                res = [s, e]
            else:
                visited.add(s)
                visited.add(e)
                uf.union(s - 1, e - 1)
        return res


if __name__ == '__main__':
    r = RedundantConnection()
    print(
        r.findRedundantConnection([[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]))
