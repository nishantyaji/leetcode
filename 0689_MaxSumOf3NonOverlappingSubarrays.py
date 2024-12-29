# Problem 689
import itertools
from typing import List


class MaxSumOf3NonOverlappingSubarrays:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        window = sum(nums[:k])
        sums = [window]
        for i in range(k, len(nums)):
            window = window - nums[i - k] + nums[i]
            sums.append(window)
        pref_max = list(itertools.accumulate(sums, max))
        pref_max = []
        this_max, this_idx = -1, -1
        for i in range(len(sums)):
            if sums[i] > this_max:
                this_max = sums[i]
                this_idx = i
            pref_max.append((this_max, this_idx))

        another = [(0, [0])] * k
        for i in range(k, len(pref_max)):
            prev = pref_max[i - k]
            another.append((prev[0] + sums[i], [prev[1], i]))

        another_max = []
        this_max, this_idx = -1, []
        for i in range(len(another)):
            if another[i][0] > this_max:
                this_max = another[i][0]
                this_idx = another[i][1]
            another_max.append((this_max, this_idx))

        this_max, res = -1, []
        for i in range(2 * k, len(sums)):
            prev = another_max[i - k]
            if sums[i] + prev[0] > this_max:
                this_max = sums[i] + prev[0]
                res = prev[1] + [i]

        return res


if __name__ == '__main__':
    m = MaxSumOf3NonOverlappingSubarrays()
    print(m.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
    print(m.maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2))
