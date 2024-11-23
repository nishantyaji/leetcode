# Problem 1072
import collections
from typing import List


class FlipColsForMaxNumOfEqRows:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cntr = collections.defaultdict(int)
        for row in matrix:
            # this row can be made homogenous
            # only if the flip columns are exactly key1 or exactly key2
            # we can find the keys shared across the row
            # We maintain the count for such key
            # Return maximum value for such a key
            key1 = "_".join(list(map(str, [i for i, x in enumerate(row) if x == 1])))
            key0 = "_".join(list(map(str, [i for i, x in enumerate(row) if x == 0])))
            cntr[key1] += 1
            cntr[key0] += 1

        return max(cntr.values())


if __name__ == '__main__':
    f = FlipColsForMaxNumOfEqRows()
    print(f.maxEqualRowsAfterFlips(
        [[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]))
    print(f.maxEqualRowsAfterFlips([[0, 1], [1, 1]]))
    print(f.maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
    print(f.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))
