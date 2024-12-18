# Problem 1284
import copy
from typing import List


class MinNumOfFlipsToConverBinMatrixTo0Matrix:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        def stringify(matr):
            key = ""
            for r in range(len(matr)):
                for c in range(len(matr[0])):
                    key += str(matr[r][c])
            return key

        dest_key = stringify(mat)
        my_dict = {}
        start = [[0 for c in range(cols)] for r in range(rows)]
        start_key = stringify(start)
        if start_key == dest_key:
            return 0
        q = [[start, 0]]

        def flip(matr, rr, cc):
            if rr > 0:
                matr[rr - 1][cc] = 1 - matr[rr - 1][cc]
            if rr < len(matr) - 1:
                matr[rr + 1][cc] = 1 - matr[rr + 1][cc]
            if cc > 0:
                matr[rr][cc - 1] = 1 - matr[rr][cc - 1]
            if cc < len(matr[0]) - 1:
                matr[rr][cc + 1] = 1 - matr[rr][cc + 1]
            matr[rr][cc] = 1 - matr[rr][cc]

        while q:
            [m2, l] = q.pop()
            for r in range(len(m2)):
                for c in range(len(m2[0])):
                    m2copy = copy.deepcopy(m2)
                    flip(m2copy, r, c)
                    key = stringify(m2copy)
                    if key == dest_key:
                        return l + 1
                    if key in my_dict:
                        continue
                    my_dict[key] = l + 1
                    q = [[m2copy, l + 1]] + q
        return -1


if __name__ == '__main__':
    m = MinNumOfFlipsToConverBinMatrixTo0Matrix()
    print(m.minFlips([[0, 0], [0, 1]]))
    print(m.minFlips([[0]]))
    print(m.minFlips([[1, 0, 0], [1, 0, 0]]))
