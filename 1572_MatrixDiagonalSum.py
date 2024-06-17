# Problem 1572
from typing import List


class MatrixDiagonalSum:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(0, len(mat)):
            result = result + mat[i][i] + mat[i][len(mat)-1-i]
        if len(mat) % 2 == 1:
            mid = int((len(mat)-1)/2)
            result = result - mat[mid][mid]
        return result


if __name__ == '__main__':
    m = MatrixDiagonalSum()
    print(m.diagonalSum([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]))
    print(m.diagonalSum([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]))
