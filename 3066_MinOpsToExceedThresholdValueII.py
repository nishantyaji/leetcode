# Problem 3066
import bisect
import heapq
from typing import List


class MinOpsToExceedThresholdValueII:

    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while nums[0] < k:
            min1 = heapq.heappop(nums)
            if nums[0] >= k:
                return res + 1
            min2 = heapq.heappop(nums)
            res += 1
            heapq.heappush(nums, 2 * min1 + min2)
        return res


    def minOperations_when_chosen_arent_2min(self, nums: List[int], k: int) -> int:
        # I initially made the wrong assumption and assumed that the chosen numbers for the operation
        # can be any number
        # the following is the approach that I came up with
        nums.sort()
        idx = bisect.bisect_right(nums, k - 1)
        nums = nums[:idx]
        if not nums:
            return 0
        end, res = 1, 0

        temp = (k - 1 - nums[-1 * end]) // 2
        idx = bisect.bisect_right(nums, temp)

        if idx >= len(nums) - end:
            res += len(nums) - end
        else:
            res += idx
            end += 1
            while len(nums) - end > idx:
                res += 1
                temp = (k - 1 - nums[-1 * end]) // 2
                idx = bisect.bisect_right(nums, temp, idx + 1)
                if len(nums) - end > idx:
                    if 2 * nums[idx] + nums[-1 * end] >= k:
                        res += 1
                        end += 1
                    else:
                        idx += 1
                        res += 1
        return res


if __name__ == '__main__':
    m = MinOpsToExceedThresholdValueII()
    print(m.minOperations([61, 8, 39, 89, 97, 79, 64, 6], 98))  # 5
    print(m.minOperations([1, 1, 2, 4, 9], 20))  # 4
    print(m.minOperations([999999999, 999999999, 999999999], 1000000000))  # 2
    print(m.minOperations([2, 11, 10, 1, 3], 10))  # 2
    print(m.minOperations([42, 46], 42)) # 0
