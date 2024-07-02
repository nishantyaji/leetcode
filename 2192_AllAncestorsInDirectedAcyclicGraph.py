# Problem 2192
import collections
from typing import List


class AllAncestorsInDirectedAcyclicGraph:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # We maintain the immediate ancestor of a node in this dictionary
        ancestors = collections.defaultdict(list)
        for e in edges:
            ancestors[e[1]].append(e[0])

        def dfs(node: int, visited: set):
            # We traverse in the dictionary and got to the ancestors of the ancestors etc
            visited.add(node)
            further = ancestors[node]
            for f in further:
                if f not in visited:
                    # we visit only ancestors that were not visited
                    dfs(f, visited)

        result = []
        for i in range(n):
            visited = {i}
            for n in ancestors[i]:
                dfs(n, visited)
            # At the end of the DFS all the ancestors, and their ancestors etc. are tracked
            visited.remove(i)
            # We remove the self node
            # and sort
            result.append(list(sorted(visited)))

        return result


if __name__ == '__main__':
    a = AllAncestorsInDirectedAcyclicGraph()
    print(a.getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
    print(a.getAncestors(5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
