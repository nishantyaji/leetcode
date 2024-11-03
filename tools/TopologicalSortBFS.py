# Refer Problem 2392
import collections


# Topological Sort BFS - known as Kahn's algo

# in_degree = an array indicating in degrees for each node
# neighbours = a HashMap recording neighbours of each node

edge = [] # given edges
in_degree = collections.defaultdict(int)
neighbours = collections.defaultdict(list)

for [out_, in_] in edge:
    in_degree[in_] += 1
    neighbours[out_].append(in_)

queue = []
for i in in_degree:
    if in_degree[i] == 0:
        queue.append(i)

while len(queue) > 0:
    node = queue.pop(0)
    for neighbour in neighbours[node]:
        in_degree[neighbour] -= 1
        if in_degree[neighbour] == 0:
            queue.append(neighbour)