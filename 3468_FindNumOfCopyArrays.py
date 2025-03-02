# Problem 3468
from typing import List


class FindNumOfCopyArrays:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        prev_u, prev_v = bounds[0]
        for i in range(1, len(original)):
            u, v = bounds[i]
            low = max(u, original[i] - original[i - 1] + prev_u)
            high = min(v, original[i] - original[i - 1] + prev_v)
            prev_u, prev_v = low, high
        return 0 if prev_v - prev_u + 1 <= 0 else prev_v - prev_u + 1
