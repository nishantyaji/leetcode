# Problem 2558
import heapq
import math
from typing import List


class TakeGiftsFromRichestPile:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = len(gifts)
        pq = []
        heapq.heapify(pq)
        for g in gifts:
            heapq.heappush(pq, -g)

        for _ in range(k):
            g = heapq.heappop(pq)
            if g == -1:
                return res
            new_g = math.floor(math.sqrt(-g))
            heapq.heappush(pq, -new_g)

        res = 0
        while pq:
            g = heapq.heappop(pq)
            res += (-g)
        return res


if __name__ == '__main__':
    t = TakeGiftsFromRichestPile()
    print(t.pickGifts([25, 64, 9, 4, 100]))
