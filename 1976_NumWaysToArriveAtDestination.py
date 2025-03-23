# Problem 1976
import collections
import copy
import heapq
import sys
from typing import List


class NumWaysToArriveAtDestination:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Djkstra
        weights, start_node, end_node, base = [], 0, n - 1, 1000000007
        adj = collections.defaultdict(dict)
        # Use dictionary instead of 2D array to avoid TLE
        for [s, e, w] in roads:
            adj[s][e] = w
            adj[e][s] = w

        rem = set(list(range(n)))
        dist = [sys.maxsize] * n
        dist[start_node] = 0
        pq = []
        heapq.heapify(pq)

        min_dist, res = [sys.maxsize] * n, [0] * n
        res[0] = 1

        while rem:
            if start_node == end_node:
                break
            rem.remove(start_node)
            if dist[start_node] <= dist[end_node]:
                for vert, wt in adj[start_node].items():
                    if vert in rem:
                        temp = wt + dist[start_node]
                        if temp < dist[vert]:
                            dist[vert] = temp
                            heapq.heappush(pq, (dist[vert], vert))
                            res[vert] = res[start_node]
                            min_dist[vert] = dist[vert]
                        elif temp == dist[vert]:
                            res[vert] += res[start_node]

            if not pq:
                break
            while pq[0][1] not in rem:
                heapq.heappop(pq)
            start_node = heapq.heappop(pq)[1]

        return res[end_node] % base

    def countPaths_slow(self, n: int, roads: List[List[int]]) -> int:

        adj = collections.defaultdict(dict)
        for [s, e, w] in roads:
            adj[s][e] = w
            adj[e][s] = w

        mp = collections.defaultdict(list)
        mp[0].append(0)

        def dfs(node1, visited1, temp):
            for a in adj[node1]:
                if a not in visited1:
                    mp[a].append(temp + adj[node1][a])
                    v_copy = copy.deepcopy(visited1)
                    v_copy.add(a)
                    dfs(a, v_copy, temp + adj[node1][a])

        st = {0}
        dfs(0, st, 0)
        res_temp = mp[n - 1]
        res_temp.sort()
        res = 0
        for i in range(len(res_temp)):
            if res_temp[i] == res_temp[0]:
                res += 1
        return res


if __name__ == '__main__':
    n = NumWaysToArriveAtDestination()
    print(n.countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                           [0, 4, 5], [4, 6, 2]]))
    print(n.countPaths(2, [[1, 0, 10]]))
    print(n.countPaths(5, [[0,1,1],[1,2,4],[0,4,3],[3,2,5],[3,4,1],[3,0,5],[1,3,1]]))
