# Problem 732
import collections
import bisect


class MyCalendarThree:

    def __init__(self):
        self.dp = collections.Counter()
        self.times = []
        self.time_set = set()

    def book(self, startTime: int, endTime: int) -> int:
        self.dp[startTime] += 1
        self.dp[endTime] -= 1
        if startTime not in self.time_set:
            bisect.insort_left(self.times, startTime)
            self.time_set.add(startTime)
        if endTime not in self.time_set:
            bisect.insort_left(self.times, endTime)
            self.time_set.add(endTime)
        res = -1
        run_cum = 0
        for t in self.times:
            run_cum += self.dp[t]
            res = max(res, run_cum)
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
