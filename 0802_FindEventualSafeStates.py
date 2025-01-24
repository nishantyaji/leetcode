# Problem 802
import collections
import functools
from typing import List


class FindEventualSafeStates:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        out_degree = collections.defaultdict(int)
        visited = set()
        for i, vals in enumerate(graph):
            out_degree[i] += len(vals)

        # Editorial has a nice solution using topological sort.
        # check : https://leetcode.com/problems/find-eventual-safe-states/editorial/?envType=daily-question&envId=2025-01-24

        @functools.cache
        def get_val(node: int):
            if not out_degree[node]:
                return True
            if node in visited:
                return False
            visited.add(node)
            for g in graph[node]:
                if not get_val(g):
                    return False
            visited.discard(node)
            return True

        res, st = [], set()
        for i in range(len(graph)):
            visited = set()
            if not out_degree[i]:
                res.append(i)
            elif get_val(i):
                res.append(i)
        return res


if __name__ == '__main__':
    f = FindEventualSafeStates()
    print(f.eventualSafeNodes([[], [0, 2, 3, 4], [3], [4], []]))  # [0,1,2,3,4]
    print(f.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))  # [4]
    print(f.eventualSafeNodes(
        [[4, 9], [3, 5, 7], [0, 3, 4, 5, 6, 8], [7, 8, 9], [5, 6, 7, 8], [6, 7, 8, 9], [7, 9], [8, 9], [9],
         []]))  # [0,1,2,3,4,5,6,7,8,9]
    print(f.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))  # [2,4,5,6]
