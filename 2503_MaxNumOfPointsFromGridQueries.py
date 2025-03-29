# Problem 2503
import bisect
import heapq
from typing import List, Tuple


class MaxNumOfPointsFromGridQueries:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        pairs = [(i, x) for i, x in enumerate(queries)]
        pairs.sort(key=lambda x: x[1])
        return self.bfs(grid, pairs)

    def bfs(self, grid: List[List[int]], queries: List[Tuple]):
        res = [0] * len(queries)
        rows, cols = len(grid), len(grid[0])
        visited = {(0, 0)}
        pq = []

        def neighbours(rr: int, cc: int, limit: int) -> List:
            neighs = []
            rest = []
            delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for (dx, dy) in delta:
                rdx, rdy = (rr + dx, cc + dy)
                if 0 <= rdx < rows and 0 <= rdy < cols and (rdx, rdy) not in visited:
                    visited.add((rdx, rdy))
                    if grid[rdx][rdy] < limit:
                        neighs.append((grid[rdx][rdy], rdx, rdy))
                    else:
                        rest.append((grid[rdx][rdy], rdx, rdy))
                        heapq.heappush(pq, (grid[rdx][rdy], rdx, rdy))
            return neighs

        flag, prev = False, 0
        for i, (place, q) in enumerate(queries):
            if grid[0][0] >= q:
                continue

            que, temp = [], 0
            if not flag:
                que = [(grid[0][0], 0, 0)]
                flag = True
            else:
                while pq and pq[0][0] < q:
                    que.append(heapq.heappop(pq))

            while que:
                (val, x, y) = que.pop()
                temp += 1
                neis = neighbours(x, y, q)
                que = neis + que
            res[place] = prev + temp
            prev = res[place]

        return res


if __name__ == '__main__':
    m = MaxNumOfPointsFromGridQueries()
    print(m.maxPoints([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2]))
    print(m.maxPoints([[5, 2, 1], [1, 1, 2]], [3]))
