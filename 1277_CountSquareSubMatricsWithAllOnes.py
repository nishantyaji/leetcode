# Problem 1277
import collections
from typing import List


class CountSquareSubMatricsWithAllOnes:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        size = min(rows, cols)
        mp = collections.defaultdict(set)

        def calc_dim(dimm: int):
            for r in range(0, rows - dimm + 1):
                for c in range(0, cols - dimm + 1):
                    mp[dimm].add((r, c))

        def remove_dim(dimm: int):
            for r in range(0, rows):
                for c in range(0, cols):
                    if matrix[r][c] == 0:
                        for x in range(max(0, r - dimm + 1), r + 1):
                            for y in range(max(0, c - dimm + 1), c + 1):
                                if (x, y) in mp[dimm]:
                                    mp[dimm].remove((x, y))
            this_val = len(mp[dimm])
            del mp[dimm]
            return this_val

        res = 0
        for i in range(1, size + 1):
            calc_dim(i)
            this_res = remove_dim(i)
            res += this_res
            if this_res == 0:
                break
        return res


    def countSquares2(self, matrix: List[List[int]]) -> int:
        # A short and elegant solution
        # as seen in the leetcode editorial
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (
                        min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    )
                    ans += dp[i + 1][j + 1]
        return ans

if __name__ == '__main__':
    c = CountSquareSubMatricsWithAllOnes()
    print(c.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
    print(c.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
