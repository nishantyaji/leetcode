# Problem 1334
import operator
from typing import List


class FindCitySmallestNumNeighboursThreshold:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        edges = [e for e in edges if e[2] <= distanceThreshold]
        adj = [[-1 for y in range(n)] for x in range(n)]
        for [s, e, d] in edges:
            adj[s][e] = d
            adj[e][s] = d
        tuples = []

        for i in range(n):
            q, visited, dist, changed, present = [i], set(), {i: 0}, True, i
            while len(visited) < n:
                inner = [(k, v) for k, v in dist.items() if k not in visited]
                if len(inner) == 0:
                    break
                inner.sort(key=operator.itemgetter(1))
                present = inner[0][0]
                visited.add(present)
                for j in range(n):
                    if j != i and j not in visited and adj[present][j] > -1:
                        temp = dist[present] + adj[present][j]
                        if temp > distanceThreshold:
                            continue
                        if j not in dist or dist[j] > temp:
                            dist[j] = temp
                            q.append(j)
            del dist[i]
            v = sum([1 for k, v in dist.items() if v <= distanceThreshold])
            tuples.append((i, v))
        tuples.sort(key=lambda t: (t[1], -t[0]))
        return tuples[0][0]


if __name__ == '__main__':
    f = FindCitySmallestNumNeighboursThreshold()
    print(f.findTheCity(6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20))
    # 5
    print(f.findTheCity(6, [[0, 3, 5], [2, 3, 7], [0, 5, 2], [0, 2, 5], [1, 2, 6], [1, 4, 7], [3, 4, 4], [2, 5, 5],
                            [1, 5, 8]], 8279))
    # 5
    print(f.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
    # 3
    print(f.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2))
    # 0
