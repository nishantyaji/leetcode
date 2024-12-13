# Problem 2593
import heapq
from typing import List


class FindScoreOfArrayAfterMarkingAllElems:
    def findScore(self, nums: List[int]) -> int:
        pq, marked, res = [], set(), 0
        heapq.heapify(pq)
        for i, n in enumerate(nums):
            heapq.heappush(pq, (1000001 * n + i, n, i))

        while len(marked) < len(nums):
            (_, n, i) = heapq.heappop(pq)
            if i not in marked:
                res += n
                marked.add(i)
                if i > 0:
                    marked.add(i - 1)
                if i < len(nums) - 1:
                    marked.add(i + 1)
        return res

if __name__ == '__main__':
    f = FindScoreOfArrayAfterMarkingAllElems()
    print(f.findScore([2,1,3,4,5,2]))
