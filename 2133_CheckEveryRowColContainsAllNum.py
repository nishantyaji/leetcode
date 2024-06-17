# Problem 2133
from typing import List


class CheckEveryRowColContainsAllNum:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        my_set = set()
        for i in range(1, len(matrix) + 1):
            my_set.add(i)

        for row in matrix:
            my_set_copy = set(my_set)
            for element in row:
                if element not in my_set_copy:
                    return False
                else:
                    my_set_copy.remove(element)

        for col in range(0, len(matrix)):
            my_set_copy = set(my_set)
            for row in range(0, len(matrix)):
                if matrix[row][col] not in my_set_copy:
                    return False
                else:
                    my_set_copy.remove(matrix[row][col])

        return True
