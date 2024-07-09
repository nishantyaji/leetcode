# Problem 1701
from typing import List


class AverageWaitingTime:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        running = customers[0][1] + customers[0][0]
        waiting = [customers[0][1]]
        for c in customers[1:]:
            this_waiting = c[1]
            if c[0] < running:
                this_waiting += (running - c[0])
                running += c[1]
            else:
                running = c[0] + c[1]
            waiting.append(this_waiting)
        return sum(waiting) / len(waiting)


if __name__ == '__main__':
    a = AverageWaitingTime()
    print(a.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
    # 5.00000
    print(a.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
    # 3.25000
