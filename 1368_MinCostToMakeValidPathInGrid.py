# Problem 1368
from typing import List


class MinCostToMakeValidPathInGrid:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = [((0, 0), 0)]
        visited = set()

        def nxt(t):
            xx, yy = t[0], t[1]
            sign = grid[xx][yy]
            if sign == 1:
                return (xx, yy + 1) if yy + 1 < cols and (xx, yy + 1) not in visited else None
            if sign == 2:
                return (xx, yy - 1) if yy > 0 and (xx, yy - 1) not in visited else None
            if sign == 3:
                return (xx + 1, yy) if xx + 1 < rows and (xx + 1, yy) not in visited else None
            if sign == 4:
                return (xx - 1, yy) if xx > 0 and (xx - 1, yy) else None

        while q:  # BFS
            (x, y), d = q.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if x == rows - 1 and y == cols - 1:
                return d

            desired = nxt((x, y))
            loops = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for lx, ly in loops:
                if 0 <= x + lx < rows and 0 <= y + ly < cols and (x + lx, y + ly) not in visited:
                    if (x + lx, y + ly) == desired:
                        if (x + lx, y + ly) == (rows - 1, cols - 1):
                            return d
                        q.append(((x + lx, y + ly), d))
                    else:
                        q = [((x + lx, y + ly), d + 1)] + q
        return -1


if __name__ == '__main__':
    m = MinCostToMakeValidPathInGrid()
    print(m.minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))  # 0
    print(m.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))  # 3
    print(m.minCost([[1, 2], [4, 3]]))  # 1
