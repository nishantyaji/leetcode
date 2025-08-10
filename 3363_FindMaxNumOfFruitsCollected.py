# Problem 3363
from typing import List


class FindMaxNumOfFruitsCollected:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        res, n = 0, len(fruits)
        for i in range(n):
            res += fruits[i][i]
            fruits[i][i] = 0

        temp = [[0 for _ in range(n)] for _ in range(n)]
        temp[n - 1][0] = fruits[n - 1][0]
        # left bot to right bot (n-1, 0) -> (n-1, n-1)
        for col in range(1, n):
            dis_from_end = min(col, n - 1 - col)
            for j in range(n - 1, n - 1 - dis_from_end - 1, -1):
                to_add = temp[j][col - 1]
                if j + 1 <= n - 1:
                    to_add = max(to_add, temp[j + 1][col - 1])
                if j - 1 >= 0:
                    to_add = max(to_add, temp[j - 1][col - 1])
                temp[j][col] = fruits[j][col] + to_add

        res += temp[n - 1][n - 1]

        temp = [[0 for _ in range(n)] for _ in range(n)]
        temp[0][n - 1] = fruits[0][n - 1]
        for row in range(1, n):
            dis_from_end = min(row, n - 1 - row)
            for i in range(n - 1, n - 1 - dis_from_end - 1, -1):
                to_add = temp[row - 1][i]
                if i + 1 <= n - 1:
                    to_add = max(to_add, temp[row - 1][i + 1])
                if i - 1 >= 0:
                    to_add = max(to_add, temp[row - 1][i - 1])
                temp[row][i] = fruits[row][i] + to_add
        res += temp[n - 1][n - 1]
        return res


if __name__ == '__main__':
    f = FindMaxNumOfFruitsCollected()
    print(f.maxCollectedFruits([[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]))  # 100
    print(f.maxCollectedFruits([[1, 1], [1, 1]]))  # 4
