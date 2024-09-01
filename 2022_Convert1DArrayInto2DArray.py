# Problem 2022
from typing import List


class Convert1DArrayInto2DArray:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        grid = [[0 for c in range(n)] for r in range(m)]
        for i, v in enumerate(original):
            grid[i // n][i % n] = v
        return grid
