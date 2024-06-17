# Problem 2958

from typing import List

class LongestSubArrayAtMostKFrequency:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        countdic = {nums[0]: 1}
        maxlen = 0
        left = 0
        for rightidx in range(1, len(nums)):
            rightval = nums[rightidx]
            if rightval in countdic:
                count = countdic[rightval]
                count += 1
                if count > k:
                    thislen = rightidx - left
                    if maxlen < thislen:
                        maxlen = thislen
                    while nums[left] != rightval and left < rightidx:
                        leftval = countdic[nums[left]]
                        countdic[nums[left]] = leftval - 1
                        left = left + 1
                    left = left + 1
                else:
                    countdic[rightval] = count
            else:
                countdic[rightval] = 1
        if maxlen == 0:
            maxlen = len(nums)
        else:
            thislen = 0
            for val in countdic.values():
                thislen += val
            if maxlen < thislen:
                maxlen = thislen
        return maxlen

if __name__ == '__main__':
    l = LongestSubArrayAtMostKFrequency()
    print(l.maxSubarrayLength([2,2,3], 1))
    print(l.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
    print(l.maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
    print(l.maxSubarrayLength([5,5,5,5,5,5,5], 4))