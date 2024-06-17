# Problem 2226

from typing import List


class MaxCandiesAllocatedToKChildren:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check_int_qs(nums: List[int], d: int, k: int) -> bool:
            return sum([x // d for x in nums]) >= k

        candies.sort()
        start, end = 1, candies[-1]
        if check_int_qs(candies, end, k):
            return end
        if not check_int_qs(candies, start, k):
            return 0
        while start <= end:
            mid = (start + end) // 2
            if check_int_qs(candies, mid, k):
                prev = mid
                start, end = mid + 1, end
            else:
                prev = start
                start, end = start, mid - 1
        return end


if __name__ == '__main__':
    m = MaxCandiesAllocatedToKChildren()
    print(m.maximumCandies([4, 7, 5], 4))
    print(m.maximumCandies([1, 2, 3, 4, 10], 5))
