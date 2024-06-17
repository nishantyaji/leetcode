# Problem 496

from typing import List


class NextGreaterElementI:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        q = []
        for n in nums2:
            while len(q) > 0 and q[-1] < n:
                popped = q.pop()
                my_dict[popped] = n
            q.append(n)

        res = []
        for n in nums1:
            res.append(-1 if n not in my_dict else my_dict[n])
        return res
