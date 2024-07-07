# Problem 1579
from typing import List


class RemoveMaxNumEdgesGraphFullyTraversible:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        type1, type2, type3 = [], [], []

        for e in edges:
            if e[0] == 1:
                type1.append((e[1], e[2]))
            elif e[0] == 2:
                type2.append((e[1], e[2]))
            else:
                type3.append((e[1], e[2]))

        result = 0
        for t in type3:
            result += alice.unionBySize(t[0] - 1, t[1] - 1)
            bob.unionBySize(t[0] - 1, t[1] - 1)
            # you can also check whether alice.is_connected.
            # But it will result in TLE.
            # Hence, check whether is_connected in the end

        for t in type2:
            result += alice.unionBySize(t[0] - 1, t[1] - 1)
            # you can also check whether alice.is_connected.
            # But it will result in TLE.
            # Hence, check whether is_connected in the end

        for t in type1:
            result += bob.unionBySize(t[0] - 1, t[1] - 1)
            # you can also check whether bob.is_connected.
            # But it will result in TLE.
            # Hence, check whether is_connected in the end

        if not alice.is_connected() or not bob.is_connected():
            return -1
        return len(edges) - result


class UnionFind:
    # copied from GFG
    def __init__(self, n):
        self.Parent = list(range(n))
        self.Size = [1] * n

    def find(self, i):
        if self.Parent[i] != i:
            # Path compression: Make the parent of i the root of the set
            self.Parent[i] = self.find(self.Parent[i])
        return self.Parent[i]

    def unionBySize(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            # return zero if this union is no-op
            return 0

        isize = self.Size[irep]
        jsize = self.Size[jrep]

        if isize < jsize:
            self.Parent[irep] = jrep
            self.Size[jrep] += self.Size[irep]
        else:
            self.Parent[jrep] = irep
            self.Size[irep] += self.Size[jrep]
        # return 1 if there is an actual merge (actual op)
        return 1

    def is_connected(self):
        for i in range(len(self.Parent)):
            self.find(i)
        my_set = set(self.Parent)
        return len(my_set) == 1


if __name__ == '__main__':
    r = RemoveMaxNumEdgesGraphFullyTraversible()
    print(r.maxNumEdgesToRemove(13,
                                [[1, 1, 2], [2, 1, 3], [3, 2, 4], [3, 2, 5], [1, 2, 6], [3, 6, 7], [3, 7, 8], [3, 6, 9],
                                 [3, 4, 10], [2, 3, 11], [1, 5, 12], [3, 3, 13], [2, 1, 10], [2, 6, 11], [3, 5, 13],
                                 [1, 9, 12], [1, 6, 8], [3, 6, 13], [2, 1, 4], [1, 1, 13], [2, 9, 10], [2, 1, 6],
                                 [2, 10, 13], [2, 2, 9], [3, 4, 12], [2, 4, 7], [1, 1, 10], [1, 3, 7], [1, 7, 11],
                                 [3, 3, 12], [2, 4, 8], [3, 8, 9], [1, 9, 13], [2, 4, 10], [1, 6, 9], [3, 10, 13],
                                 [1, 7, 10], [1, 1, 11], [2, 4, 9], [3, 5, 11], [3, 2, 6], [2, 1, 5], [2, 5, 11],
                                 [2, 1, 7], [2, 3, 8], [2, 8, 9], [3, 4, 13], [3, 3, 8], [3, 3, 11], [2, 9, 11],
                                 [3, 1, 8], [2, 1, 8], [3, 8, 13], [2, 10, 11], [3, 1, 5], [1, 10, 11], [1, 7, 12],
                                 [2, 3, 5], [3, 1, 13], [2, 4, 11], [2, 3, 9], [2, 6, 9], [2, 1, 13], [3, 1, 12],
                                 [2, 7, 8], [2, 5, 6], [3, 1, 9], [1, 5, 10], [3, 2, 13], [2, 3, 6], [2, 2, 10],
                                 [3, 4, 11], [1, 4, 13], [3, 5, 10], [1, 4, 10], [1, 1, 8], [3, 3, 4], [2, 4, 6],
                                 [2, 7, 11], [2, 7, 10], [2, 3, 12], [3, 7, 11], [3, 9, 10], [2, 11, 13], [1, 1, 12],
                                 [2, 10, 12], [1, 7, 13], [1, 4, 11], [2, 4, 5], [1, 3, 10], [2, 12, 13], [3, 3, 10],
                                 [1, 6, 12], [3, 6, 10], [1, 3, 4], [2, 7, 9], [1, 3, 11], [2, 2, 8], [1, 2, 8],
                                 [1, 11, 13], [1, 2, 13], [2, 2, 6], [1, 4, 6], [1, 6, 11], [3, 1, 2], [1, 1, 3],
                                 [2, 11, 12], [3, 2, 11], [1, 9, 10], [2, 6, 12], [3, 1, 7], [1, 4, 9], [1, 10, 12],
                                 [2, 6, 13], [2, 2, 12], [2, 1, 11], [2, 5, 9], [1, 3, 8], [1, 7, 8], [1, 2, 12],
                                 [1, 5, 11], [2, 7, 12], [3, 1, 11], [3, 9, 12], [3, 2, 9], [3, 10, 11]]))
    # 114
    print(r.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 3, 4], [1, 1, 3], [2, 2, 4]]))
    # 0
    print(r.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))
    # 2
    print(r.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))
    # 0
    print(r.maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]))
    # -1
