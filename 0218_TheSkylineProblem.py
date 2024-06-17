# Problem 218
import collections
from typing import List


class TheSkylineProblem:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        max_x = max(list(map(lambda x: x[1], buildings)))
        markers = collections.defaultdict(list)
        for building in buildings:
            markers[building[0]].append(building[2])
            markers[building[1]].append(-building[2])

        keys = list(markers.keys())
        keys.sort()
        running_list = []
        result = []
        for k in keys:
            vals = markers[k]
            for v in vals:
                if v > 0:
                    running_list.append(v)
                else:
                    running_list.remove(-v)
            height = 0 if len(running_list) == 0 else max(running_list)
            if len(result) == 0 or result[-1][1] != height:
                result.append([k, height])
        if len(result) > 0 and result[-1][1] != 0:
            result.append([max_x, 0])
        return result


if __name__ == '__main__':
    t = TheSkylineProblem()
    print(t.getSkyline([[2, 9, 10], [9, 12, 15]]))
    # [[2,10],[9,15],[12,0]]

    print(t.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    print(t.getSkyline([[0, 2, 3], [2, 5, 3]]))
