# Problem 826

import bisect
import operator
from typing import List


class MostProfitAssigningEvent:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # There is a memoization (counting sort) solution in the leetcode editorial
        # please do take a look
        if min(difficulty) > max(worker):
            return 0
        worker.sort()
        result, end, prof_n_diff = 0, len(profit), sorted(zip(profit, difficulty), key=operator.itemgetter(0), reverse=True)
        for pnd in prof_n_diff:
            w_index = bisect.bisect_left(worker, pnd[1])
            if w_index != len(worker):
                result += (len(worker) - w_index) * pnd[0]
                worker = worker[:w_index]
                if not worker:
                    break
        return result


if __name__ == '__main__':
    m = MostProfitAssigningEvent()
    print(m.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
    # 100
    print(m.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))
    # 0

