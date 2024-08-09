# Problem 840
from typing import List


class MagicSquaresInGrid:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        cum = 0
        for r in range(rows):
            for c in range(cols):
                if self.is_magic(grid, r, c):
                    cum += 1

        return cum

    def is_magic(self, grid: List[List[int]], row: int, col: int):
        rows, cols = len(grid), len(grid[0])
        if row >= rows - 2 or col >= cols - 2:
            return False

        uniq = set()
        for r in range(3):
            for c in range(3):
                uniq.add(grid[row + r][col + c])

        if uniq != set(list(range(1, 10))):
            return False

        ops = [[[0, 0], [0, 1], [0, 2]],
               [[1, 0], [1, 1], [1, 2]],
               [[2, 0], [2, 1], [2, 2]],

               [[0, 0], [1, 0], [2, 0]],
               [[0, 1], [1, 1], [2, 1]],
               [[0, 2], [1, 2], [2, 2]],

               [[0, 0], [1, 1], [2, 2]],
               [[0, 2], [1, 1], [2, 0]]]

        sumset = set()
        for st1 in ops:
            sm = 0
            for st2 in st1:
                sm += grid[row + st2[0]][col + st2[1]]
            sumset.add(sm)
        if len(sumset) > 1:
            return False

        return True


if __name__ == '__main__':
    m = MagicSquaresInGrid()
    print(m.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
    print(m.numMagicSquaresInside([[8]]))
