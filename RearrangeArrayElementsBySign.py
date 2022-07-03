# Problem 2149

from typing import List


class RearrangeArrayElementsBySign:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIdx = 0
        negIdx = 1
        result = [None] * len(nums)
        for num in nums:
            if num > 0:
                result[posIdx] = num
                posIdx = posIdx + 2
            else:
                result[negIdx] = num
                negIdx = negIdx + 2
        return result


if __name__ == '__main__':
    r = RearrangeArrayElementsBySign()
    print(r.rearrangeArray([3, 1, -2, -5, 2, -4]))
    print(r.rearrangeArray([-1, 1]))
