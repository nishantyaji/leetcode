# Problem 731
import bisect


class MyCalendarTwo:

    def __init__(self):
        self.slots1 = []
        self.slots2 = []

    def is_overlap(self, s1: list[int], s2: list[int]):
        if (s1[1] > s2[0] >= s1[0]) or (s2[1] > s1[0] >= s2[0]):
            return True
        return False

    def get_window(self, s1: list[int], s2: list[int]):
        return [max(s1[0], s2[0]), min(s1[1], s2[1])]

    def book(self, start: int, end: int) -> bool:
        for s in self.slots2:
            if self.is_overlap([start, end], s):
                return False

        in_first = False
        for s in self.slots1:
            if self.is_overlap([start, end], s):
                overlap_window = self.get_window(s, [start, end])
                bisect.insort_left(self.slots2, overlap_window, key=lambda x: x[0])

        # always insert in the first slot
        bisect.insort_left(self.slots1, [start, end], key=lambda x: x[0])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    m = MyCalendarTwo()
    # slots = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    slots = [[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
    for [start, end] in slots:
        print(m.book(start, end))
