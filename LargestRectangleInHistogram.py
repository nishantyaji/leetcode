# Problem 84
from typing import List


class LargestRectangleInHistogram:

    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for idx, i in enumerate(heights):
            if idx == 0 or i > stack[-1][1]:
                # if the element is higher than the top of the stack
                stack.append([idx, i])
            else:
                while len(stack) > 0 and stack[-1][1] >= i:
                    # find out the height which was just breached by a smaller number
                    [pop_idx, pop_height] = stack.pop()
                    # the width of the height is the index if the stack is empty
                    # otherwise it is idx - 1 - stack[-1][0]
                    # -1 because idx does not have pop_height but is the one that breaches it
                    # Note that if there are 3 occurrences of 4 continuously then
                    # the stack has the right most occurrence of 4
                    # therefore you can just take the diff between the indices of the top 2 stack elements
                    diff = idx if not stack else idx - stack[-1][0] - 1
                    area = pop_height * diff
                    if max_area < area:
                        max_area = area
                stack.append([idx, i])

        return max_area


if __name__ == '__main__':
    l = LargestRectangleInHistogram()
    # print(l.largestRectangleArea())
    print(l.largestRectangleArea([2, 1, 2]))
    print(l.largestRectangleArea([2, 4]))
    print(l.largestRectangleArea([2, 1, 5, 6, 2, 3]))
