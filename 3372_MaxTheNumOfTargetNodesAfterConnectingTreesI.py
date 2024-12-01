# Problem 3372
import collections
from typing import List


class MaxTheNumOfTargetNodesAfterConnectingTreesI:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Floyd warshall takes O(n^3)
        # BFS takes O(V(V+E)) = O(2N^2) = O(n^2). Note E = V-1 because tree
        # Hence in this case BFS is faster
        # For a complete graph you could say FW and BFS might be proximate in complexity

        size1, size2 = len(edges1) + 1, len(edges2) + 1
        adj1, adj2 = [[] for _ in range(size1)], [[] for _ in range(size2)]
        for s, e in edges2:
            adj2[s].append(e)
            adj2[e].append(s)

        # Usage of adjacency matrix results in Memory Limit Exceeded
        def bfs_inner(l, adj, start):
            dq = collections.deque()
            visited = set()
            dq.append((start, 0))
            while dq:
                v, d = dq.popleft()  # vertex, distance
                if d == l + 1:
                    break
                visited.add(v)
                for a in adj[v]:
                    if a not in visited:  # this is critical
                        dq.append((a, d + 1))
            res_inner = len(visited)
            del visited
            return res_inner

        max_k1 = -1
        for i in range(size2):
            max_k1 = max(max_k1, bfs_inner(k - 1, adj2, i))
        del adj2
        for s, e in edges1:
            adj1[s].append(e)
            adj1[e].append(s)
        if k == 0:
            return [1] * size1
        res = []
        for i in range(size1):
            res.append(max_k1 + bfs_inner(k, adj1, i))
        del adj1
        return res

    def floyd_warshall(self, dist, v):
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == '__main__':
    m = MaxTheNumOfTargetNodesAfterConnectingTreesI()
    print(
        m.maxTargetNodes([[0, 1], [0, 2], [2, 3], [2, 4]], [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], 2))
    print(m.maxTargetNodes([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]], 1))
