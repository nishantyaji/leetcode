# Problem 1944
from typing import List


class NumVisiblePeopleInQueue:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack, rev_vals = [], []
        for i in range(len(heights) - 1, - 1, -1):
            temp = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                temp += 1
            if stack:
                # you can still see the stack element, so add
                temp += 1
            stack.append(heights[i])
            rev_vals.append(temp)
        return rev_vals[::-1]


if __name__ == '__main__':
    n = NumVisiblePeopleInQueue()
    print(n.canSeePersonsCount([4, 3, 2, 1]))  # [1,1,1,0]
    print(n.canSeePersonsCount([5, 1, 2, 3, 10]))  # [4,1,1,1,0]
    print(n.canSeePersonsCount([10, 6, 8, 5, 11, 9]))  # [3,1,2,1,1,0]
