# Problem 352
from typing import List


class DataStreamAsDisjointedIntervals:
    def __init__(self):
        self.list_windows = []

    def addNum(self, value: int) -> None:
        if len(self.list_windows) == 0:
            self.list_windows.append([value, value])
            return

        if len(self.list_windows) == 1:
            if value == self.list_windows[0][0] - 1:
                prev = self.list_windows.pop(0)
                self.list_windows.append([value, prev[1]])
            elif value == self.list_windows[0][1] + 1:
                prev = self.list_windows.pop(0)
                self.list_windows.append([prev[0], value])
            else:
                if value > self.list_windows[0][1] + 1:
                    self.list_windows.append([value, value])
                elif value < self.list_windows[0][0] - 1:
                    self.list_windows.insert(0, [value, value])
            return

        start, end = 0, len(self.list_windows) - 1

        merged = False
        while start <= end:
            mid = (start + end) // 2
            if self.list_windows[mid][0] - 1 <= value <= self.list_windows[mid][1] + 1:
                if value in [self.list_windows[mid][0] - 1, self.list_windows[mid][1] + 1]:
                    self.merge(value, mid, value == self.list_windows[mid][0] - 1)
                merged = True
                break
            elif value > self.list_windows[mid][1] + 1:
                start = mid + 1
            else:
                end = mid - 1

        if not merged:
            self.list_windows.insert(start, [value, value])
        return None

    def merge(self, value: int, index: int, before: bool):
        [neighbour, modify_pair, diff] = [index - 1, 1, -1] if before else [index + 1, 0, 1]

        if len(self.list_windows) > neighbour >= 0 and self.list_windows[neighbour][modify_pair] == value + diff:
            self.list_windows[neighbour][modify_pair] = self.list_windows[index][modify_pair]
            self.list_windows.pop(index)
        else:
            self.list_windows[index][0 if before else 1] = value

    def getIntervals(self) -> List[List[int]]:
        print(self.list_windows)
        return self.list_windows


if __name__ == '__main__':
    summaryRanges = DataStreamAsDisjointedIntervals()
    summaryRanges.addNum(6)
    summaryRanges.getIntervals()
    summaryRanges.addNum(6)
    summaryRanges.getIntervals()
    summaryRanges.addNum(0)
    summaryRanges.getIntervals()
    summaryRanges.addNum(4)
    summaryRanges.getIntervals()
    summaryRanges.addNum(8)
    summaryRanges.getIntervals()
    summaryRanges.addNum(7)
    summaryRanges.getIntervals()
    summaryRanges.addNum(6)
    summaryRanges.getIntervals()
    summaryRanges.addNum(4)
    summaryRanges.getIntervals()
    summaryRanges.addNum(7)
    summaryRanges.getIntervals()
    summaryRanges.addNum(5)
    summaryRanges.getIntervals()

    summaryRanges = DataStreamAsDisjointedIntervals()
    summaryRanges.addNum(1)
    summaryRanges.getIntervals()
    summaryRanges.addNum(0)
    summaryRanges.getIntervals()

    summaryRanges = DataStreamAsDisjointedIntervals()
    summaryRanges.addNum(1)
    # arr = [1]
    summaryRanges.getIntervals()
    # return [[1, 1]]
    summaryRanges.addNum(3)
    # arr = [1, 3]
    summaryRanges.getIntervals()
    # // return [[1, 1], [3, 3]]
    summaryRanges.addNum(7)
    # // arr) = [1, 3, 7]
    summaryRanges.getIntervals()
    # // return [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)
    # // arr = [1, 2, 3, 7]
    summaryRanges.getIntervals()
    # // return [[1, 3], [7, 7]]
    summaryRanges.addNum(6)
    # arr = [1, 2, 3, 6, 7]
    summaryRanges.getIntervals()
    # // return [[1, 3], [6, 7]]
