# Problem 2290
import collections
import heapq
import sys
from typing import List


class MinObstacleRemovalToReachCorner:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def value(_r, _c):
            return cols * _r + _c

        # djkstra
        pq = []
        heapq.heapify([pq])
        adj = collections.defaultdict(dict)
        for r in range(rows):
            for c in range(cols):
                val_rc = value(r, c)
                if c < cols - 1:
                    adj[val_rc][value(r, c + 1)] = grid[r][c + 1]
                    adj[value(r, c + 1)][val_rc] = grid[r][c]
                if r < rows - 1:
                    adj[val_rc][value(r + 1, c)] = grid[r + 1][c]
                    adj[value(r + 1, c)][val_rc] = grid[r][c]

        heapq.heappush(pq, (0, 0))
        end_val = value(rows - 1, cols - 1)
        visited = set()
        distance_dict = collections.defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                distance_dict[value(r, c)] = sys.maxsize
        distance_dict[0] = 0

        while pq[0][1] != end_val:
            distance, node = heapq.heappop(pq)
            visited.add(node)
            neis = adj[node].keys() - visited
            for nei in neis:
                temp = adj[node][nei] + distance_dict[node]
                if temp < distance_dict[nei]:
                    distance_dict[nei] = temp
                    heapq.heappush(pq, (distance_dict[nei], nei))

        return heapq.heappop(pq)[0]


if __name__ == '__main__':
    m = MinObstacleRemovalToReachCorner()
    print(m.minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
    print(m.minimumObstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))
