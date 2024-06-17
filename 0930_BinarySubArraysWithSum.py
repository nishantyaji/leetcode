# problem 930
from typing import List


# Somehow solved this question in first attempt. A lot of scope of improvement

# Revise

class BinarySubArraysWithSum:

    def goal_zero(self, nums: List[int]):
        this_sum = 0
        count = 0
        for i in nums:
            if i > 0:
                this_sum = this_sum + int((count * (count + 1)) / 2)
                count = 0
            else:
                count = count + 1

        if nums[-1] == 0:
            this_sum = this_sum + int((count * (count + 1)) / 2)

        return this_sum

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            return self.goal_zero(nums)

        window_indices = [-1] * (goal + 1)
        sum = 0
        for idx in range(0, len(nums)):
            if nums[idx] == 1:
                prev = window_indices.pop(0)
                window_indices.append(idx)
                if len(window_indices) == goal + 1 and window_indices[0] > -1:
                    sum += (window_indices[0] - prev) * (window_indices[goal] - window_indices[goal - 1])
        sum += (window_indices[1] - window_indices[0]) * (len(nums) - window_indices[goal])
        return sum


if __name__ == '__main__':
    b = BinarySubArraysWithSum()
    print(b.numSubarraysWithSum([0, 1, 1, 1, 1], 3))
    print(b.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
    print(b.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
