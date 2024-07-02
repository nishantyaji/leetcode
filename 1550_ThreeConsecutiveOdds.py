# Problem 1550
import collections
from typing import List


class ThreeConsecutiveOdds:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        dq = collections.deque()
        dq.append(False)
        dq.append(False)
        for i in range(len(arr)):
            if arr[i] % 2 == 1 and dq[0] and dq[1]:
                return True
            dq.popleft()
            dq.append(arr[i] % 2 == 1)
        return False
