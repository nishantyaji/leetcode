# Problem 1854
from typing import List


class MaximumPopulationYear:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = []
        base = 1950
        for i in range(1950, 2050):
            arr.append(0)
        for [born, dead] in logs:
            for i in range(born, dead):
                arr[i-base] = arr[i-base]+1
        max_pop = 0
        max_year = 1949
        for i in range(1950, 2050):
            if arr[i-base] > max_pop:
                max_pop = arr[i-base]
                max_year = i

        return max_year


if __name__ == '__main__':
    m = MaximumPopulationYear()
    print(m.maximumPopulation([[1993, 1999], [2000, 2010]]))
    print(m.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]))
