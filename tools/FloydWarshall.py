import sys

n = 10  # num nodes
dist = [[sys.maxsize for x in range(n)] for y in range(n)]

# Floyd warshall : we calculate the (adj matrix) ** n
for k in range(n):  # intermediate
    for i in range(n):  # source node
        for j in range(n):  # destination node
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# Note that the intermediate node appears in the outer for loop
# and then the source node
# and the inner for loop is the destination node
