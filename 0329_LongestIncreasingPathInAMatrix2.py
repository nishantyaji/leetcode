# Problem 329
from typing import List


class LongestIncreasingPathInAMatrix:

    def __init__(self):
        self.cache = {}

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_length = -1
        for rowIndex in range(0, len(matrix)):
            for colIdx in range(0, len(matrix[rowIndex])):
                traversed = [[0] * len(matrix[rowIndex])
                             for _ in range(len(matrix))]

                length = self.traverse(rowIndex, colIdx, matrix)
                if length > max_length:
                    max_length = length
        return max_length

    def traverse(self, presentRow: int, presentCol: int, matrix: List[List[int]]) -> int:
        presentVal = matrix[presentRow][presentCol]
        # left
        if presentCol > 0 and matrix[presentRow][presentCol-1] < presentVal:
            left_count = self.cacheReturn(presentRow, presentCol-1, matrix) + 1
        else:
            left_count = 1
        # right
        if presentCol < len(matrix[0]) - 1 and matrix[presentRow][presentCol+1] < presentVal:
            right_count = self.cacheReturn(
                presentRow, presentCol+1, matrix) + 1
        else:
            right_count = 1
        # top
        if presentRow > 0 and matrix[presentRow-1][presentCol] < presentVal:
            top_count = self.cacheReturn(presentRow-1, presentCol, matrix) + 1
        else:
            top_count = 1
        # bottom
        if presentRow < len(matrix) - 1 and matrix[presentRow+1][presentCol] < presentVal:
            bottom_count = self.cacheReturn(
                presentRow+1, presentCol, matrix) + 1
        else:
            bottom_count = 1

        return max([left_count, right_count, top_count, bottom_count])

    def cacheReturn(self, row: int, col: int, matrix: List[List[int]]) -> int:
        if row in self.cache.keys():
            if col in self.cache[row].keys():
                return self.cache[row][col]
        val = self.traverse(row, col, matrix)
        if row in self.cache.keys():
            if col in self.cache[row].keys():
                return self.cache[row][col]
            else:
                self.cache[row][col] = {}
        else:
            self.cache[row] = {}
            self.cache[row][col] = {}
        self.cache[row][col] = val
        return val


if __name__ == '__main__':
    l = LongestIncreasingPathInAMatrix()
    print(l.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print(l.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    print(l.longestIncreasingPath([[1]]))
