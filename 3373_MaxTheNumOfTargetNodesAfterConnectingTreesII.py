# Problem 3373
import collections
from typing import List


class MaxTheNumOfTargetNodesAfterConnectingTreesII:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adj1 = collections.defaultdict(list)
        adj2 = collections.defaultdict(list)

        tree1_sz = 0
        for s, e in edges1:
            adj1[s].append(e)
            adj1[e].append(s)
            tree1_sz = max(s, e, tree1_sz)

        tree2_sz = 0
        for s, e in edges2:
            adj2[s].append(e)
            adj2[e].append(s)
            tree2_sz = max(s, e, tree2_sz)

        def find_vals(adj):
            visited = set()
            q = [(0, True)]  # (node, isZero)
            zero, nonzero = set(), set()
            while q:
                v, flag = q.pop()
                visited.add(v)
                if flag:
                    zero.add(v)
                else:
                    nonzero.add(v)
                next_v = [(a, not flag) for a in adj[v] if a not in visited]
                q = next_v + q
            return [zero, nonzero]

        [tree1_zero, tree1_nonzero] = find_vals(adj1)
        [tree2_zero, tree2_nonzero] = find_vals(adj2)
        max2 = max(len(tree2_zero), len(tree2_nonzero))

        res = []
        for i in range(tree1_sz + 1):
            if i in tree1_zero:
                res.append(max2 + len(tree1_zero))
            else:
                res.append(max2 + len(tree1_nonzero))
        return res


if __name__ == '__main__':
    m = MaxTheNumOfTargetNodesAfterConnectingTreesII()
    print(m.maxTargetNodes([[0, 1], [0, 2], [2, 3], [2, 4]], [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]))
    print(m.maxTargetNodes([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]]))
