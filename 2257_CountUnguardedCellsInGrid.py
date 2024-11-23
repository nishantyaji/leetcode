# Problem 2257
from typing import List


class CountUnguardedCellsInGrid:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        # One of my least favourite problem.
        # Constraints are right.
        # Even though my previous original solution was with the same complexity
        # It was found to be very slow
        # Had to be unblocked by a hint

        for [r, c] in walls:
            grid[r][c] = 2

        for [r, c] in guards:
            # up
            grid[r][c] = 3

        for [r, c] in guards:
            for i in range(c - 1, -1, -1):
                if grid[r][i] in [2, 3]:
                    break
                grid[r][i] = 1

            # down
            for i in range(c + 1, n):
                if grid[r][i] in [2, 3]:
                    break
                grid[r][i] = 1

            # left
            for i in range(r - 1, -1, -1):
                if grid[i][c] in [2, 3]:
                    break
                grid[i][c] = 1

            # right
            for i in range(r + 1, m):
                if grid[i][c] in [2, 3]:
                    break
                grid[i][c] = 1

        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    c = CountUnguardedCellsInGrid()
    print(c.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))
    print(c.countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]))
