# Problem 2140
import functools
from typing import List


class SolvingQuestionsWithBrainpower:

    def mostPoints(self, questions: List[List[int]]) -> int:

        @functools.cache
        def calc(i: int):

            if i >= len(questions):
                return 0
            if questions[i][1] + i + 1 >= len(questions):
                return max(questions[i][0], calc(i + 1))

            calc1 = calc(questions[i][1] + i + 1) + questions[i][0]
            calc2 = calc(i + 1)
            return max(calc1, calc2)

        return calc(0)


if __name__ == '__main__':
    s = SolvingQuestionsWithBrainpower()
    print(s.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))  # 5
    print(s.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))  # 7
