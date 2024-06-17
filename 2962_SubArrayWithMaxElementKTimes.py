# Problem 2962
from typing import List

class SubArrayWithMaxElementKTimes:
    def getMaxElementIndices(self, nums: List[int], maxelem: int) -> List[int]:
        result = []
        for idx in range(0, len(nums)):
            if nums[idx] == maxelem:
                result.append(idx)
        return result

    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0

        maxelem = max(nums)
        maxelemindices = self.getMaxElementIndices(nums, maxelem)
        result = 0
        prevLeftIdx = -1
        for leftIdx in range(0, len(maxelemindices) - k + 1, 1):
            leftVal = maxelemindices[leftIdx]
            rightVal = maxelemindices[leftIdx + k - 1]

            rightsidepossibilities = len(nums) - rightVal
            leftsidepossibilities = leftVal - prevLeftIdx
            result += (rightsidepossibilities * leftsidepossibilities)
            prevLeftIdx = leftVal
        return result



if __name__ == '__main__':
    s = SubArrayWithMaxElementKTimes()
    print(s.countSubarrays([2,2,2,2,1,3,3,2,2,1,1,3,1,1,2,3,2,1,1,2,1,1,2,1,2,1,2,1,3,1,3,3]
, 5))
    print(s.countSubarrays([1,3,2,3,3], 2))
    print(s.countSubarrays([1,4,2,1], 3))