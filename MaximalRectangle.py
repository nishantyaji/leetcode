# Problem 85
from typing import List


class MaximalRectangle:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        max_area = 0
        rows = len(matrix)
        columns = len(matrix[0])
        cum_row_sum = [[0] * columns for i in range(rows)]

        for r in range(0, rows):
            for c in range(0, columns):
                if c == 0:
                    cum_row_sum[r][c] = 1 if matrix[r][c] == '1' else 0
                else:
                    if matrix[r][c] == '0':
                        cum_row_sum[r][c] = 0
                    else:
                        cum_row_sum[r][c] = cum_row_sum[r][c - 1] + 1

        print(cum_row_sum)

        for c in range(0, columns):
            new_list =[]
            for r in range(0, rows):
                new_list.append(cum_row_sum[r][c])
            max_area_this_col = self.largestRectangleArea(new_list)
            max_area = max(max_area, max_area_this_col)

        return max_area

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
    m = MaximalRectangle()
    # print(m.max_area_from_list([1, 0, 2, 3, 4, 2]))
    # print(m.maximalRectangle())
    print(m.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
    print(m.maximalRectangle([["0","0","1"],["1","1","1"]]))
    print(m.maximalRectangle([["1", "0", "1", "1"]]))
