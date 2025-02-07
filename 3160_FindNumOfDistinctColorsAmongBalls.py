# Problem 3160 : Find the number of Distinct colors among the balls

import collections
from typing import List


class FindNumOfDistinctColorsAmongBalls:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mp, vals_dict = {}, {}

        def change(index, val):  # Use count instead of set
            if index in vals_dict:
                prev_val = vals_dict[index]
                mp[prev_val] = mp[prev_val] - 1
                if mp[prev_val] == 0:
                    del mp[prev_val]
            if val not in mp:
                mp[val] = 0
            mp[val] += 1
            vals_dict[index] = val
            return len(mp)

        res = []
        for ball, color in queries:
            res.append(change(ball, color))
        return res

    def queryResults_slow_old(self, limit: int, queries: List[List[int]]) -> List[int]:
        my_map = dict()
        dict_of_set = collections.defaultdict(set)
        result = []
        for q in queries:
            if q[0] in my_map:
                q1prev = my_map[q[0]]
                dict_of_set[q1prev].remove(q[0])
                if len(dict_of_set[q1prev]) == 0:
                    del dict_of_set[q1prev]
            my_map[q[0]] = q[1]
            dict_of_set[q[1]].add(q[0])
            result.append(len(dict_of_set))
        return result


if __name__ == '__main__':
    b = FindNumOfDistinctColorsAmongBalls()
    print(b.queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
    print(b.queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
