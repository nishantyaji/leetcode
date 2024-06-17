# Problem 523
import collections
from typing import List


class ContinuousSubarraySum:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) >= 2 * k + 1:
            return True

        my_map = collections.defaultdict(list)
        cum_sum_k, my_map[0] = 0, [-1]
        for idx, num in enumerate(nums):
            cum_sum_k = (cum_sum_k + num) % k
            my_map[cum_sum_k].append(idx)
            if len(my_map[cum_sum_k]) == 3 or (
                    len(my_map[cum_sum_k]) == 2 and my_map[cum_sum_k][1] > my_map[cum_sum_k][0] + 1):
                return True
        return False


if __name__ == '__main__':
    c = ContinuousSubarraySum()
    print(c.checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(c.checkSubarraySum([23, 2, 6, 4, 7], 6))
    print(c.checkSubarraySum([23, 2, 6, 4, 7], 13))
