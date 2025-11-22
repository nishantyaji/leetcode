# Problem 1437
from typing import List


class CheckIfAll1sAreAtLeastLenKPlacesAway:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k - 1
        for i, c in enumerate(nums):
            if c == 1:
                print(prev, "-", i)
                if abs(prev - i) <= k:
                    return False
                prev = i
        return True
