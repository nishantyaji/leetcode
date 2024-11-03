import collections

edges = [[1, 2]]
num_vertices = 10
nodes = list(range(1, num_vertices + 1))
visited = {}
neighbours = collections.defaultdict(list)

for [start, end] in edges:
    neighbours[start].append(end)


def topological_sort():
    for node in nodes:
        if visited[node] is False:
            dfs(node)


ret_ordered = []


def dfs(node, ret_ordered):
    visited[node] = True
    for nei in neighbours[node]:
        dfs(nei)
    # pre-append ret_ordered in place
    ret_ordered.reverse()
    ret_ordered.append(node)
    ret_ordered.reverse()


print(ret_ordered)
