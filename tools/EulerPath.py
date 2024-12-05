"""

3 possible methods

1) Post order DFS
2) Hierholzer's Algorithm
3) Fleury Algorithm


Precondition that a Euler tour (cycle) exists:

1) Directed: The outdegree = indegree for all vertices. Or all except 2.
One vertex has outdegree = indegree + 1. This is the start
Another vertex has indegree = outdegree + 1. This will be the end
If there are no aberrations from outdegree = indegree,
then start or end can be anything

2) Undirected: All nodes have even degree. Or 2 nodes have odd degree and rest have even.

"""
import collections
from typing import List

"""
Post Order DFS
"""
def findItinerary_DFS(self, tickets: List[List[str]]) -> List[str]:
    start = "JFK"
    old_adj = collections.defaultdict(list)
    for t in tickets:
        old_adj[t[0]].append(t[1])
    adj = collections.defaultdict(collections.deque)
    for k, v in old_adj.items():
        v.sort()
        for vv in v:
            adj[k].append(vv)

    # Follow the post order DFS mentioned here:
    # https://leetcode.com/problems/valid-arrangement-of-pairs/editorial/
    trail = []

    def post_order_dfs(node):
        while adj[node]:
            # popping in necessary
            # because the same node can appear again
            # in another dept
            nei = adj[node].popleft()
            post_order_dfs(nei)
        trail.append(node)

    post_order_dfs(start)
    return list(reversed(trail))


"""
Hierholzer's Algo

"""

def hierholzer(start, adj):
    stack = [start]
    res = []
    # Iterative DFS using stack
    while stack:
        node = stack[-1]
        if adj[node]:
            # Visit the next node
            nextNode = adj[node].pop(0)
            stack.append(nextNode)
        else:
            # No more neighbors to visit, add node to result
            res.append(node)
            stack.pop()
    return res

def hierholzer2(self, adj, start):
    if len(adj) == 0:
        return
    curr_path = [start]
    circuit = []

    while curr_path:
        curr_v = curr_path[-1]
        if curr_v in adj and adj[curr_v]:
            next_v = adj[curr_v].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())

    return circuit


"""

Fleury's algo

"""

# TBD