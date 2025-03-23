# Problem 2685
import collections
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


class CountNumOfCompleteComponents:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for [s, e] in edges:
            uf.union(s, e)

        comps = [uf.find(i) for i in range(n)]
        v_counter = collections.Counter(comps)
        e_counter = collections.Counter()
        for [s, e] in edges:
            e_counter[comps[s]] += 1

        res = 0
        for k, v in v_counter.items():
            e = e_counter[k]
            if v * (v - 1) == 2 * e:
                res += 1
        return res


if __name__ == '__main__':
    c = CountNumOfCompleteComponents()
    print(c.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
    print(c.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
