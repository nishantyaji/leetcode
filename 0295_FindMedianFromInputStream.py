# Problem 295

#Very inefficient algo esp in addNum
#Needs refining

class FindMedianFromInputStream:

    def __init__(self):
        self.window = []

    def addNum(self, num: int) -> None:
        if len(self.window) == 0:
            self.window.append(num)
            return

        if num < self.window[0]:
            self.window = [num] + self.window
            return

        if num > self.window[-1]:
            self.window = self.window + [num]
            return

        [low, high] = [0, len(self.window) - 1]
        req_idx = -1

        while low + 1 < high:
            mid = int((low + high) / 2)
            if self.window[mid] == num:
                req_idx = mid
                break
            if self.window[mid] > num:
                [low, high] = [low, mid]
            else:
                [low, high] = [mid, high]

        if req_idx == -1:
            req_idx = low

        self.window = self.window[:req_idx + 1] + [num] + self.window[req_idx + 1:]

    def findMedian(self) -> float:
        if len(self.window) % 2 == 1:
            return self.window[int((len(self.window) - 1) / 2)]
        else:
            return (self.window[int(len(self.window) / 2)] + self.window[int(len(self.window) / 2) - 1]) / 2


if __name__ == '__main__':
    medianFinder = FindMedianFromInputStream()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
