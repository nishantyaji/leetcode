# Problem 3074
from typing import List


class AppleRedistributionIntoBoxes:

    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_count = sum(apple)
        capacity.sort(reverse=True)
        cum, i = 0, 0
        while cum < apple_count:
            cum += capacity[i]
            i += 1

        return i
