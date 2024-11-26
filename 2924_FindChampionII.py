# Problem 2924

from typing import List


class DSU:

    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, i: int):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i: int, j: int):
        i_par, j_par = self.find(i), self.find(j)
        i_sz, j_sz = self.size[i_par], self.size[j_par]
        if j_sz > i_sz:
            self.parents[i] = j_par
            self.size[j_par] += i_sz
        else:
            self.parents[j] = i_par
            self.size[i_par] += j_sz


class FindChampionII:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        start, end, dsu = set(), set(), DSU(n)
        for [s, e] in edges:
            start.add(s)
            end.add(e)
            dsu.union(s, e)

        for i in range(n):
            dsu.find(i)

        if len(start - end) == 1 and len(set(dsu.parents)) == 1:
            return list(start - end)[0]
        else:
            return -1


if __name__ == '__main__':
    f = FindChampionII()
    print(f.findChampion(4, [[1, 0], [2, 3], [1, 2]]))
    print(f.findChampion(3, [[0, 1], [2, 1], [0, 2]]))
