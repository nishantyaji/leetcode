# Dijkstra Algo
import collections
import heapq

# BIDIRECTIONAL
edges = [[]]  # [[v1, v2], [v3, v7] .. ]
weights = []
start_node = 0
end_node = 10
n = 11  # number of nodes

adj = collections.defaultdict(dict)
# Use dictionary instead of 2D array to avoid TLE
for i, e in enumerate(edges):
    adj[e[0]][e[1]] = weights[i]
    adj[e[1]][e[0]] = weights[i]

rem = set(list(range(n)))
dist = [0] * n
dist[start_node] = 0
pq = []
heapq.heapify(pq)

while rem:
    if start_node == end_node:
        break

    rem.remove(start_node)
    for vert, wt in adj[start_node].items():
        if vert in rem:
            temp = wt + dist[start_node]
            if temp < dist[vert]:
                dist[vert] = temp
                # min heap
                heapq.heappush(pq, (dist[vert], vert))

    if not pq:
        break
    while pq[0][1] not in rem:
        heapq.heappop(pq)
    start_node = heapq.heappop(pq)[1]

print(dist[end_node])
