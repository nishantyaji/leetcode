# problem 931

from typing import List
class MinimumFallingPathSum:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cumsum = a = [[0 for _ in range(0, rows)] for y in range(0, cols)]

        for i in range(0, cols):
            cumsum[0][i] = matrix[0][i]

        for i in range(1, rows):
            for j in range(0, cols):
                min_list = []
                if j > 0:
                    min_list.append(cumsum[i - 1][j - 1])
                if j < cols - 1:
                    min_list.append(cumsum[i - 1][j + 1])
                min_list.append(cumsum[i - 1][j])

                cumsum[i][j] = matrix[i][j] + min(min_list)

        return min(cumsum[rows - 1])
