# Problem 1292
from typing import List


class MaxSideLengthOfASquareWithSumLTEThreshold:

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        rowsum = [[0 for _ in range(cols)] for _ in range(rows)]

        # Row sum is sub-optimal
        # Use Rectangle
        # if the top-left corner of the rectangle is (x1, y1) and the bottom-right corner is (x2, y2), then the sum of elements in this region is:
        # sum = A[x1..x2][y1..y2] = P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
        for r in range(rows):
            cumsum = 0
            for c in range(cols):
                cumsum += mat[r][c]
                rowsum[r][c] = cumsum

        max_side = min(rows, cols)
        s, e = 1, max_side
        st = set()
        while s <= e:
            m = (s + e) // 2
            if self.check(rowsum, rows, cols, m, threshold):
                st.add(m)
                s = m + 1
            else:
                e = m - 1

        return 0 if not st else max(st)

    def check(self, rowsum: List[int], rows: int, cols: int, side: int, threshold: int):
        for c in range(0, cols - side + 1):
            for r in range(0, rows - side + 1):
                sq_sum = 0
                for i in range(0, side):
                    low = 0 if c == 0 else rowsum[r + i][c - 1]
                    temp = rowsum[r + i][c + side - 1] - low
                    sq_sum += temp
                    if sq_sum > threshold:
                        continue
                if sq_sum <= threshold:
                    return True
        return False


if __name__ == '__main__':
    m = MaxSideLengthOfASquareWithSumLTEThreshold()
    print(m.maxSideLength([[0]], 0))
    print(m.maxSideLength([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4))  # 2
    print(m.maxSideLength([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1))  # 0
