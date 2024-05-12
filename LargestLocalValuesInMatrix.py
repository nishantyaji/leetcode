# Problem 2373


from typing import List


class LargestLocalValuesInMatrix:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        sz = len(grid)
        res = [[0 for x in range(sz - 2)] for y in range(sz - 2)]

        for i in range(1, sz - 1):
            for j in range(1, sz - 1):
                res[i - 1][j - 1] = max(grid[i][j], grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i - 1][j - 1],
                                        grid[i + 1][j - 1], grid[i][j + 1], grid[i - 1][j + 1], grid[i + 1][j + 1])

        return res
