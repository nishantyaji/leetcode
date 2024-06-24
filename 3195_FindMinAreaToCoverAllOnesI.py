# Problem 3195
import math
from typing import List


class FindMinAreaToCoverAllOnesI:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_x, min_y, max_x, max_y = math.inf, math.inf, -1, -1
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    min_x = min(min_x, i)
                    max_x = max(max_x, i)
                    min_y = min(min_y, j)
                    max_y = max(max_y, j)
        return (max_x - min_x + 1) * (max_y - min_y + 1)
