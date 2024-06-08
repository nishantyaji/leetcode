# Problem 3162

from typing import List


class FindTheNumberOfGoodPairsI:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        nums2 = [k * n for n in nums2]
        for x in nums1:
            for y in nums2:
                result += 1 if x % y == 0 else 0
        return result


if __name__ == '__main__':
    w = FindTheNumberOfGoodPairsI()
    print(w.numberOfPairs([1, 3, 4], [1, 3, 4], 1))
    print(w.numberOfPairs([1, 2, 4, 12], [2, 4], 3))
    # print(w.numberOfPairs())
