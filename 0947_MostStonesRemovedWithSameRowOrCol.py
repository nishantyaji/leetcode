# Problem 947
import collections
from typing import List


class MostStonesRemovedWithSameRowOrCol:

    def removeStones(self, stones: List[List[int]]) -> int:
        x_mp = collections.defaultdict(list)
        y_mp = collections.defaultdict(list)

        for i in range(len(stones)):
            x_mp[stones[i][0]].append(i)
            y_mp[stones[i][1]].append(i)

        dsu = UnionBySize(len(stones))
        for x, indices in x_mp.items():
            for j in range(len(indices)):
                dsu.union(indices[j - 1], indices[j])
        for y, indices in y_mp.items():
            for j in range(len(indices)):
                dsu.union(indices[j - 1], indices[j])

        for i in range(len(stones)):
            dsu.find(i)

        parents = set(dsu.parent)
        return len(stones) - len(parents)


class UnionBySize:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.sz = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        par_i, par_j = self.find(i), self.find(j)
        if par_i == par_j:
            return
        if self.sz[j] > self.sz[i]:
            self.parent[par_i] = par_j
            self.sz[j] += self.sz[i]
        else:
            self.parent[par_j] = par_i
            self.sz[i] += self.sz[j]


if __name__ == '__main__':
    m = MostStonesRemovedWithSameRowOrCol()
    print(m.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
    print(m.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
    print(m.removeStones([[0, 0]]))
