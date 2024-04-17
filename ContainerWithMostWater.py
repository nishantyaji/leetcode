# Problem 11
from typing import List


class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = max_area = 0
        right_ptr = len(height) - 1

        while left_ptr < right_ptr:
            area = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            max_area = max(area, max_area)
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_area


if __name__ == '__main__':
    c = ContainerWithMostWater()
    print(c.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(c.maxArea([1, 1]))
