# Problem 1051
import copy
from typing import List


class HeightChecker:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = copy.deepcopy(heights)
        sorted_heights.sort()
        return sum([1 for idx, num in enumerate(heights) if num != sorted_heights[idx]])
