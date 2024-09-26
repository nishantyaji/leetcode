# Problem 729
import bisect


class MyCalendar:

    def __init__(self):
        self.slots = []

    def book(self, start: int, end: int) -> bool:
        if not self.slots:
            self.slots.append([start, end])
            return True
        starts = list(map(lambda x: x[0], self.slots))
        ends = list(map(lambda x: x[1], self.slots))

        start_idx = bisect.bisect_left(starts, start)
        if start_idx == 0:
            if starts[start_idx] == start or end > starts[start_idx]:
                return False
        elif start_idx == len(self.slots):
            if ends[len(self.slots) - 1] > start:
                return False
        else:
            if starts[start_idx] == start or start < ends[start_idx - 1] or end > starts[start_idx]:
                return False

        bisect.insort_left(self.slots, [start, end], key=lambda x: x[0])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    m = MyCalendar()
    slots = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    for [start, end] in slots:
        print(m.book(start, end))
