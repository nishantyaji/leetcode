# Problem 3218
import operator
from typing import List


class MinCostForCuttingCakeI:

    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        h_tuples = [[x, "h"] for x in horizontalCut]
        v_tuples = [[x, "v"] for x in verticalCut]
        tuples = h_tuples + v_tuples
        tuples.sort(key=operator.itemgetter(0), reverse=True)
        h_count, v_count, cost = 1, 1, 0
        for t in tuples:
            if t[1] == "h":
                mul = v_count
                h_count += 1
            else:
                mul = h_count
                v_count += 1
            cost += t[0] * mul
        return cost


if __name__ == '__main__':
    m = MinCostForCuttingCakeI()
    print(m.minimumCost(3, 2, [1, 3], [5]))
    print(m.minimumCost(2, 2, [7], [4]))
