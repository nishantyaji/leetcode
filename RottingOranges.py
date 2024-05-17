# Problem 994

from typing import List


class RottingOranges:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        one_set = set()
        rotten = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c, 0])
                elif grid[r][c] == 1:
                    one_set.add((r, c))

        max_count = 0
        while rotten:
            [r, c, count] = rotten.pop(0)
            max_count = max(max_count, count)
            adj = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            for radj, cadj in adj:
                if 0 <= radj < rows and 0 <= cadj < cols and (radj, cadj) in one_set:
                    rotten.append([radj, cadj, count + 1])
                    one_set.remove((radj, cadj))

        if len(one_set) > 0:
            return -1
        else:
            return max_count
