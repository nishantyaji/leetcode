# Problem 1552
from typing import List


class MagneticForceBetweenTwoBalls:

    def maxDistance(self, position: List[int], m: int) -> int:
        # Had to take a hint that is binary search based problem
        # otherwise tough nut to crack

        position.sort()
        # left should not be zero. The diff (i.e result) that we are finding
        # is not a function of the starting element
        # diff can be smaller than position[0]
        left, right = 0, position[-1]
        my_dict = {left: True}
        while left <= right:
            mid = left + (right - left) // 2
            if self.check_cdn(position, m, mid):
                my_dict[mid] = True
                left = mid + 1
            else:
                right = mid - 1
        return max(my_dict)

    def check_cdn(self, position: List[int], m: int, k: int):
        prev = position[0]
        for p in position[1:]:
            if p - prev >= k:
                m -= 1
                prev = p
            if m == 1:
                break
        return m == 1


if __name__ == '__main__':
    m = MagneticForceBetweenTwoBalls()
    print(m.maxDistance([1, 2, 3, 4, 7], 3))
    # 3
    print(m.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))
    # 999999999
    print(m.maxDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
    # 3
    print(m.maxDistance([79, 74, 57, 22], 4))
