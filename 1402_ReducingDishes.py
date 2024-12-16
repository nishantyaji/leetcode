# Problem 1402
from typing import List


class ReducingDishes:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # O(n^2) complexity.
        satisfaction.sort(reverse=True)
        res = 0
        for i in range(len(satisfaction), 0, -1):
            muls = list(range(1, i + 1))[::-1]
            temp = list(zip(muls, satisfaction))
            temp_res = sum([a * b for (a, b) in temp])
            res = max(res, temp_res)
        return res

    def maxSatisfactionQuick(self, satisfaction: List[int]) -> int:
        # O(n) time complexity
        satisfaction.sort(reverse=True)
        res = 0
        run_sum = 0
        cum_sum = 0
        for i in range(len(satisfaction)):
            cum_sum += satisfaction[i]
            run_sum += cum_sum
            res = max(res, run_sum)

        return res


if __name__ == '__main__':
    r = ReducingDishes()
    print(r.maxSatisfaction([-1, -8, 0, 5, -9]))
    print(r.maxSatisfactionQuick([-1, -8, 0, 5, -9]))
    print(r.maxSatisfaction([4, 3, 2]))
    print(r.maxSatisfactionQuick([4, 3, 2]))
    print(r.maxSatisfaction([-1, -4, -5]))
    print(r.maxSatisfactionQuick([-1, -4, -5]))
