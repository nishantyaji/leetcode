# Problem 3142

from typing import List


class CheckIfGridSatisfiesConditions:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        for i in range(0, rows):
            for j in range(0, cols):
                if i != rows - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                if j != cols - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
        return True


if __name__ == '__main__':
    c = CheckIfGridSatisfiesConditions()
    print(c.satisfiesConditions([[0, 4, 1, 7, 5, 4, 1, 4, 0, 7]]))
    print(c.satisfiesConditions([[1, 0, 2], [1, 0, 2]]))
    print(c.satisfiesConditions([[1, 1, 1], [0, 0, 0]]))
    print(c.satisfiesConditions([[1], [2], [3]]))
    print(c.satisfiesConditions([[1]]))
