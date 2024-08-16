# Problem 624
import collections
import sys
from typing import List


class MaxDistInArrays:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        mins, maxs = [sys.maxsize, sys.maxsize], [-10001, -10001]

        def ins_min(n: int):
            if n <= mins[0]:
                mins[1] = mins[0]
                mins[0] = n
            elif n < mins[1]:
                mins[1] = n

        def ins_max(n: int):
            if n >= maxs[0]:
                maxs[1] = maxs[0]
                maxs[0] = n
            elif n > maxs[1]:
                maxs[1] = n

        maxp = collections.defaultdict(list)
        for i in arrays:
            ins_min(i[0])
            ins_max(i[-1])
            maxp[i[-1]].append(i[0])

        if len(maxp[maxs[0]]) > 1 or maxp[maxs[0]][0] != mins[0]:
            diff = abs(maxs[0] - mins[0])
        else:
            diff = max(maxs[0] - mins[1], maxs[1] - mins[0])
        return diff


if __name__ == '__main__':
    m = MaxDistInArrays()
    print(m.maxDistance([[1, 5], [4, 4]]))
    print(m.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
    print(m.maxDistance([[1], [1]]))
