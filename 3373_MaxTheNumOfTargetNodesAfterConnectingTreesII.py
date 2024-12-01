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

        for s, e in edges2:
            adj2[s].append(e)
            adj2[e].append(s)

        def find_vals(adj):
            visited = set()
            q = [(0, 0)]  # (node, isZero)
            set_list = [set(), set()]  # set_list[0] has nodes at even distance from 0,
            while q:
                v, flag = q.pop()
                set_list[flag % 2].add(v)
                visited.add(v)
                next_v = [(a, not flag) for a in adj[v] if a not in visited]
                q = next_v + q
            return set_list

        [tree1_zero, tree1_nonzero] = find_vals(adj1)
        [tree2_zero, tree2_nonzero] = find_vals(adj2)
        max2 = max(len(tree2_zero), len(tree2_nonzero))
        return [max2 + (len(tree1_zero) if i in tree1_zero else len(tree1_nonzero)) for i in range(tree1_sz + 1)]


if __name__ == '__main__':
    m = MaxTheNumOfTargetNodesAfterConnectingTreesII()
    print(m.maxTargetNodes([[0, 1], [0, 2], [2, 3], [2, 4]], [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]))
    print(m.maxTargetNodes([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]]))
