# Problem 1514
import collections
import heapq
from typing import List


class PathWithMaxProbability:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # Dijkstra's algo
        adj = collections.defaultdict(dict)
        # Use dictionary instead of 2D array to avoid TLE
        for i, e in enumerate(edges):
            adj[e[0]][e[1]] = succProb[i]
            adj[e[1]][e[0]] = succProb[i]

        rem = set(list(range(n)))
        dist = [0.0] * n
        dist[start_node] = 1.0
        pq = []
        heapq.heapify(pq)

        while rem:
            if start_node == end_node:
                break

            rem.remove(start_node)
            for vert, prob in adj[start_node].items():
                if vert in rem and prob > 0.0:
                    temp = prob * dist[start_node]
                    if temp > dist[vert]:
                        dist[vert] = temp
                        heapq.heappush(pq, (-dist[vert], vert))

            if not pq:
                break
            while pq[0][1] not in rem:
                heapq.heappop(pq)
            start_node = heapq.heappop(pq)[1]

        return dist[end_node]


if __name__ == '__main__':
    p = PathWithMaxProbability()
    print(p.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
    # 0.250
    print(p.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
    # Output: 0.30000
    print(p.maxProbability(3, [[0, 1]], [0.5], 0, 2))
    # 0.00
