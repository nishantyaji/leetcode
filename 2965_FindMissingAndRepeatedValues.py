# Problem 2965
from typing import List


class FindMissingAndRepeatedValues:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rows, cols, every, res = len(grid), len(grid[0]), set(), [None, None]
        every = set(range(1, rows * cols + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] not in every:
                    res[0] = grid[r][c]
                every.discard(grid[r][c])
        res[1] = list(every)[0]
        return res
