# Problem 3143
import collections
from typing import List


class MaxPointsInSquare:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        my_dict = collections.defaultdict(list)
        for i in range(0, len(points)):
            sq_side_half = max(abs(points[i][0]), abs(points[i][1]))
            my_dict[s[i]].append(sq_side_half)

        min_of_min = 1000000001
        new_dict = {}
        for k in my_dict.keys():
            vals = my_dict[k]
            vals.sort()
            if len(vals) > 1:
                if min_of_min > vals[1]:
                    min_of_min = vals[1]
            new_dict[k] = vals[0]

        return len([v for k, v in new_dict.items() if v < min_of_min])


if __name__ == '__main__':
    m = MaxPointsInSquare()
    print(m.maxPointsInsideSquare([[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], "abdca"))
    print(m.maxPointsInsideSquare([[1, 1], [-2, -2], [-2, 2]], "abb"))
    print(m.maxPointsInsideSquare([[1, 1], [-1, -1], [2, -2]], "ccd"))
