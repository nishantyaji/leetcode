# Problem 1975
import sys
from typing import List


class MaxMatrixSum:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sm, rows, cols, num_neg, smallest = 0, len(matrix), len(matrix[0]), 0, sys.maxsize
        """
        This problem can be solved by a trick
        
        If there are 2 adjacent negatives you can cancel 2 negatives
        If there is a dangling negative you can move the negative sign to any place
        You can move many dangling negatives together just beside each other
        
        You can use the adjacent logic again and cancel.
        We see that if there even number of negative numbers then all can be cancelled
        Otherwise there will be one negative number remaining
        You must ideally have the negative sign against the number having lowest absolute value
        """
        for r in range(rows):
            for c in range(cols):
                sm += abs(matrix[r][c])
                num_neg += (1 if matrix[r][c] < 0 else 0)
                smallest = min(smallest, abs(matrix[r][c]))

        return sm if num_neg % 2 == 0 else sm - 2 * smallest


if __name__ == '__main__':
    m = MaxMatrixSum()
    print(m.maxMatrixSum([[1, -1], [-1, 1]]))
    print(m.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
