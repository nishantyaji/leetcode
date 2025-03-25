# Problem 3394
from typing import List


class CheckIfGridCanBeCutToSections2:

    def check_1D(self, arr, n) -> bool:
        gaps = 0
        prev = arr[0][1]
        for i in range(1, len(arr)):
            if arr[i][0] >= prev:
                gaps += 1
                if gaps == 2:
                    return True
            prev = max(prev, arr[i][1])
        return False

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs, ys = [], []
        for r in rectangles:
            xs.append((r[0], r[2]))
            ys.append((r[1], r[3]))
        xs.sort(key=lambda x: (x[0], -x[1]))
        ys.sort(key=lambda x: (x[0], -x[1]))

        if self.check_1D(xs, n):  # horizontal scan
            return True
        return self.check_1D(ys, n)


if __name__ == '__main__':
    c = CheckIfGridCanBeCutToSections2()
    print(c.checkValidCuts(3, [[0, 0, 1, 3], [1, 0, 2, 2], [2, 0, 3, 2], [1, 2, 3, 3]]))  # False
    print(c.checkValidCuts(4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))  # False
    print(c.checkValidCuts(4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))  # True
    print(c.checkValidCuts(6, [[4, 0, 5, 2], [0, 5, 4, 6], [4, 5, 6, 6]]))  # False
    print(c.checkValidCuts(5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))  # True
