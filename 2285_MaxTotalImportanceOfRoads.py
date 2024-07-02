# Problem 2285
import collections
import operator
from typing import List


class MaxTotalImportanceOfRoads:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cntr = collections.defaultdict(int)
        for i in range(n):
            cntr[i] = 0
        for r in roads:
            cntr[r[0]] += 1
            cntr[r[1]] += 1
        cntr_items = sorted(cntr.items(), key=operator.itemgetter(1))
        node_vals = {x[0]: i + 1 for i, x in enumerate(cntr_items)}
        return sum([node_vals[r[0]] + node_vals[r[1]] for r in roads])


if __name__ == '__main__':
    m = MaxTotalImportanceOfRoads()
    print(m.maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
    print(m.maximumImportance(5, [[0, 3], [2, 4], [1, 3]]))
    print(m.maximumImportance(5, [[0, 1]]))
    # 9
