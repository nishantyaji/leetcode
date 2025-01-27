# Problem 1462
from typing import List


class CourseScheduleIV:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        #Floyd Warshall
        dp = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for pre, pos in prerequisites:
            dp[pre][pos] = True
        for k in range(numCourses):  # intermediate
            for i in range(numCourses):  # source node
                for j in range(numCourses):  # destination node
                    dp[i][j] = dp[i][k] & dp[k][j] or dp[i][j]
        res = []
        for u, v in queries:
            res.append(dp[u][v])
        return res


if __name__ == '__main__':
    c = CourseScheduleIV()
    print(c.checkIfPrerequisite(11,
                                [[6, 3], [6, 8], [6, 5], [6, 10], [6, 0], [6, 7], [6, 4], [6, 9], [6, 1], [3, 8],
                                 [3, 10], [3, 0], [3, 7],
                                 [3, 4], [3, 2], [3, 9], [3, 1], [8, 5], [8, 10], [8, 4], [8, 2], [8, 9], [5, 10],
                                 [5, 7], [5, 4], [5, 9],
                                 [5, 1], [10, 0], [10, 7], [10, 4], [10, 2], [10, 9], [0, 7], [0, 4], [0, 2], [7, 2],
                                 [7, 9], [7, 1], [4, 2],
                                 [4, 9], [4, 1], [2, 9], [2, 1]],
                                [[2, 1], [8, 9], [6, 7], [3, 8], [4, 10], [9, 6], [4, 2], [5, 10], [3, 5], [5, 9],
                                 [10, 7], [7, 6], [7, 10],
                                 [0, 5], [2, 8], [6, 2], [9, 7], [9, 4], [5, 0], [9, 5], [0, 9], [6, 10], [8, 9],
                                 [5, 8], [8, 9], [4, 5],
                                 [1, 10], [6, 5], [5, 9], [0, 9], [2, 6], [4, 5], [9, 1], [8, 1], [9, 10], [4, 6],
                                 [6, 4], [5, 9], [7, 1],
                                 [10, 1], [9, 6], [1, 3], [2, 0], [9, 10], [5, 9], [7, 5], [9, 6], [1, 4], [3, 1],
                                 [10, 4], [5, 6], [1, 4],
                                 [4, 3], [9, 5], [4, 5], [5, 8], [5, 6], [9, 10], [9, 10], [7, 8], [5, 6], [4, 6],
                                 [3, 5], [7, 10], [8, 10],
                                 [7, 8], [0, 4], [7, 0], [8, 3], [8, 10], [2, 4], [6, 10], [0, 1], [10, 6], [7, 2],
                                 [4, 3], [2, 3], [3, 1],
                                 [1, 4], [5, 7], [4, 10], [7, 2], [6, 8], [0, 8], [4, 3], [8, 7], [0, 3], [10, 9],
                                 [5, 7], [6, 8], [8, 5],
                                 [3, 5], [9, 5], [7, 9], [7, 9], [3, 4], [7, 6], [3, 9], [2, 0], [10, 6], [7, 6],
                                 [10, 6], [4, 3], [9, 10],
                                 [3, 7], [7, 10], [6, 1]]))
    print(c.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))  # [False, True]
    print(c.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]))  # [False, False]
    print(c.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))  # [True, True]
