# Problem 2560
import sys
from typing import List


class HouseRobberIV:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check_possible(limit: int) -> bool:
            prev, kk = -2, k

            for i, x in enumerate(nums):
                if x <= limit:
                    if prev != i - 1:
                        kk -= 1
                        if kk == 0:
                            return True
                        prev = i
            return kk == 0

        res, s, e = sys.maxsize, min(nums), max(nums)

        while s <= e:
            mid = (s + e) // 2
            temp = check_possible(mid)
            if temp:
                res = min(res, mid)
                e = mid - 1
            else:
                s = mid + 1
        return res


if __name__ == '__main__':
    h = HouseRobberIV()
    print(h.minCapability([2, 3, 5, 9], 2))  # 5
    print(h.minCapability([2, 7, 9, 3, 1], 2))  # 2
