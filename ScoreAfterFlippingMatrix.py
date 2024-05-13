# Problem 861

from typing import List


class ScoreAfterFlippingMatrix:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # row flips
        col_sum = [0] * cols
        for r in range(rows):
            do_flip = grid[r][0] == 0
            for c in range(cols):
                if do_flip:
                    grid[r][c] = grid[r][c] ^ 1
                col_sum[c] += grid[r][c]

        # col flips and sum
        result = 0
        base2 = 1
        for c in range(cols - 1, -1, -1):
            multiplicand = col_sum[c] if 2 * col_sum[c] >= rows else (rows - col_sum[c])
            result += multiplicand * base2
            base2 = base2 << 1
        return result


if __name__ == '__main__':
    s = ScoreAfterFlippingMatrix()
    print(s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
