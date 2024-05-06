# Problem 503
from typing import List


class NextGreaterElementII:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        res = [-1] * len(nums)

        nums2 = nums * 2
        q = []
        for idx, n in enumerate(nums2):
            while len(q) > 0 and q[-1][1] < n:
                [popped_idx, popped_val] = q.pop()
                if popped_idx < len(nums):
                    res[popped_idx] = n
            q.append([idx, n])

        return res


if __name__ == '__main__':
    n = NextGreaterElementII()
    print(n.nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))
