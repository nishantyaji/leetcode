# Problem 332
import collections
from typing import List


class ReconstructItinerary:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        start = "JFK"
        old_adj = collections.defaultdict(list)
        for t in tickets:
            old_adj[t[0]].append(t[1])
        adj = collections.defaultdict(collections.deque)
        for k, v in old_adj.items():
            v.sort()  # sorting to maintain lexicographic order
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


if __name__ == '__main__':
    r = ReconstructItinerary()
    print(r.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(r.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(r.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
