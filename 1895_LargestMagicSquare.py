# Problem 1895
from typing import List


class LargestMagicSquare:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rowsum = [[0 for _ in range(cols)] for _ in range(rows)]
        colsum = [[0 for _ in range(rows)] for _ in range(cols)]

        for r in range(rows):
            cumsum = 0
            for c in range(cols):
                cumsum += grid[r][c]
                rowsum[r][c] = cumsum

        for c in range(cols):
            cumsum = 0
            for r in range(rows):
                cumsum += grid[r][c]
                colsum[c][r] = cumsum

        max_side = min(rows, cols)

        for side in range(max_side, 1, -1):

            for c in range(0, cols - side + 1):
                for r in range(0, rows - side + 1):
                    low = 0 if c == 0 else rowsum[r][c - 1]
                    ref = rowsum[r][c + side - 1] - low
                    possible_for_r_c = True
                    for i in range(1, side):
                        low = 0 if c == 0 else rowsum[r + i][c - 1]
                        temp = rowsum[r + i][c + side - 1] - low
                        if temp != ref:
                            possible_for_r_c = False
                            break
                    if not possible_for_r_c:
                        continue

                    low = 0 if r == 0 else colsum[c][r - 1]
                    reftemp = colsum[c][r + side - 1] - low
                    if reftemp != ref:
                        continue
                    for i in range(1, side):
                        low = 0 if r == 0 else colsum[c + i][r - 1]
                        temp = colsum[c + i][r + side - 1] - low
                        if temp != ref:
                            possible_for_r_c = False
                            break
                    if not possible_for_r_c:
                        continue

                    diagonal1 = 0
                    for i in range(side):
                        diagonal1 += grid[r + i][c + i]

                    diagonal2 = 0
                    for i in range(side):
                        diagonal2 += grid[r + i][c + side - 1 - i]

                    if diagonal1 == diagonal2 == ref:
                        return side
        return 1


if __name__ == '__main__':
    l = LargestMagicSquare()
    print(l.largestMagicSquare([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]))
    print(l.largestMagicSquare([[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]))
