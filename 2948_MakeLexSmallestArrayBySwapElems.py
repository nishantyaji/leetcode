# Problem 2948
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


class MakeLexSmallestArrayBySwapElems:

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = [(x, i) for i, x in enumerate(nums)]
        pairs.sort(key=lambda x: x[0])
        n = len(nums)
        uf = UnionFind(n)
        for i, (num, idx) in enumerate(pairs):
            if i == 0:
                continue
            if num - pairs[i - 1][0] <= limit:
                uf.union(pairs[i][1], pairs[i - 1][1])

        for i in range(n):
            uf.find(i)

        elems = collections.defaultdict(list)
        for i in range(n):
            elems[uf.parent[i]].append(nums[i])

        for k, v in elems.items():
            elems[k].sort(reverse=True)

        res = []
        for i in range(n):
            res.append(elems[uf.parent[i]].pop())
        return res


if __name__ == '__main__':
    m = MakeLexSmallestArrayBySwapElems()
    print(
        m.lexicographicallySmallestArray([1, 60, 34, 84, 62, 56, 39, 76, 49, 38], 4))  # [1,56,34,84,60,62,38,76,49,39]
    print(m.lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], 3))  # [1,6,7,18,1,2]
    print(m.lexicographicallySmallestArray([1, 5, 3, 9, 8], 2))  # [1,3,5,8,9]
    print(m.lexicographicallySmallestArray([1, 7, 28, 19, 10], 3))  # [1,7,28,19,10]
