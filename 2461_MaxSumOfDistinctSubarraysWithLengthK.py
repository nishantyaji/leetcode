# Problem 2461
from typing import List


class MaxSumOfDistinctSubarraysWithLengthK:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {}
        others = {"amount": 0, "total": 0}

        def add_(numm):
            if numm not in my_dict:
                my_dict[numm] = 0
            my_dict[numm] += 1
            others["amount"] += 1
            others["total"] += numm

        def rem_(numm):
            if numm in my_dict:
                my_dict[numm] -= 1
                if my_dict[numm] == 0:
                    del my_dict[numm]
                others["amount"] -= 1
                others["total"] -= numm

        def check_():
            return others["amount"] == k and len(my_dict) == k

        for i in range(0, k):
            add_(nums[i])

        max_ = 0
        if check_():
            max_ = max(max_, others["total"])

        for i in range(k, len(nums)):
            rem_(nums[i - k])
            add_(nums[i])
            if check_():
                max_ = max(max_, others["total"])

        return max_
