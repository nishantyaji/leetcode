# Problem 3097
import sys
from typing import List


class ShortestSubarrayWithORAtLeastKII:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        k_bits = k.bit_length()
        max_bits = max([i.bit_length() for i in nums])
        if k_bits > max_bits:
            return -1
        window, left, right = [0] * 33, 0, 0

        def add_(numm):
            num_str = format(numm, "b")
            for i, x in enumerate(num_str[::-1]):
                if x == "1":
                    window[i] += 1

        def rem_(numm):
            num_str = format(numm, "b")
            for i, x in enumerate(num_str[::-1]):
                if x == "1":
                    window[i] -= 1

        def check_():
            win_str = "".join(["1" if x > 0 else "0" for x in window])[::-1]
            win_val = 0 if not win_str else int(win_str, 2)
            return win_val >= k

        min_res = sys.maxsize
        add_(nums[0])
        while right < len(nums):
            while check_():
                min_res = min(min_res, right - left + 1)
                rem_(nums[left])
                left += 1

            right += 1
            if right < len(nums):
                add_(nums[right])

        return min_res if min_res < sys.maxsize else -1


if __name__ == '__main__':
    s = ShortestSubarrayWithORAtLeastKII()
    print(s.minimumSubarrayLength(
        [536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288,
         262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0],
        1000000000))
    print(s.minimumSubarrayLength([1, 12, 26, 2], 8))
    print(s.minimumSubarrayLength([41], 3))
    print(s.minimumSubarrayLength([1, 2, 3], 2))
    print(s.minimumSubarrayLength([2, 1, 8], 10))
    print(s.minimumSubarrayLength([1, 2], 0))
