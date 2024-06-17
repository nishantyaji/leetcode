# Problem 713
from typing import List
class SubArrayProductLessThanK:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        result = 0

        product = 1
        left = 0
        for i in range(0, len(nums)):
            product = product * nums[i]
            while product >= k:
                product /= nums[left]
                left += 1
                if left > i:
                    break
            result += (i - left + 1)
        return result


        return result

if __name__ == '__main__':
    s = SubArrayProductLessThanK()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
    print(s.numSubarrayProductLessThanK([1,2,3], 0))