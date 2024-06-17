# 3159. Find Occurrences of an Element in an Array
from typing import List


class FindOccurrencesOfElemInArray:

    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        xs = [idx for idx, num in enumerate(nums) if num == x]
        return [-1 if q > len(xs) else xs[q - 1] for q in queries]


if __name__ == '__main__':
    b = FindOccurrencesOfElemInArray()
