# Problem 875
import bisect
import math
from typing import List


class KokoEatingBananas:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        # In fact there is no need to sort depending on the test cases
        # O(nlogn) is the sorting alog
        # Without sorting the complexity is O(nlogh)

        s, e = 1, max(piles)
        res = -1
        while s <= e:
            mid = (s + e) // 2
            v = self.num_hours(piles, mid)
            if v <= h:
                res = mid
                e = mid - 1
            else:
                s = mid + 1
        return res

    def num_hours(self, piles, speed: int):
        idx = bisect.bisect_left(piles, speed)
        if idx == len(piles):
            return len(piles)

        res = idx  # count the ones that are <= speed as 1 hour
        for i in range(idx, len(piles)):
            res += (math.ceil(piles[i] / speed))

        return res

if __name__ == '__main__':
    k = KokoEatingBananas()
    print(k.minEatingSpeed([3,6,7,11], 8))
    print(k.minEatingSpeed([30,11,23,4,20], 5))
    print(k.minEatingSpeed([30,11,23,4,20], 6))