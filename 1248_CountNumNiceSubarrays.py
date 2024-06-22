# Problem 1248
import collections
from typing import List


class CountNumNiceSubarrays:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)
        mp[0] = 1
        run_count, result = 0, 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                run_count += 1
            mp[run_count] += 1
        for i in range(0, run_count - k + 1):
            result += mp[i] * mp[i + k]
        return result


if __name__ == '__main__':
    c = CountNumNiceSubarrays()
    print(c.numberOfSubarrays([1, 1, 2, 1, 1], 3))
    # 2
    print(c.numberOfSubarrays([2, 4, 6], 1))
    # 0
    print(c.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
    # 16

if __name__ == '__main__':
    c = CountNumNiceSubarrays()
