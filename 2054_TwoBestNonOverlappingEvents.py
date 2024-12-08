# Problem 2054
from typing import List


class TwoBestNonOverlappingEvents:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts, ends, times = [], [], set()
        for [s, e, v] in events:
            starts.append([s, v])
            ends.append([e, v])
            times.add(s)
            times.add(e)

        starts.sort(reverse=True)
        ends.sort()
        times = sorted(list(times))

        idx, max_suff, new_starts = 0, 0, []
        for t in times[::-1]:
            while idx < len(starts) and t == starts[idx][0]:
                max_suff = max(max_suff, starts[idx][1])
                idx += 1
            new_starts.append(max_suff)
        new_starts.reverse()

        idx, max_pref, new_ends = 0, 0, []
        for t in times:
            while idx < len(ends) and t == ends[idx][0]:
                max_pref = max(max_pref, ends[idx][1])
                idx += 1
            new_ends.append(max_pref)

        max_all = new_ends[-1]
        for i in range(0, len(times) - 1):
            max_all = max(max_all, new_ends[i] + new_starts[i + 1])
        return max_all


if __name__ == '__main__':
    t = TwoBestNonOverlappingEvents()
    print(t.maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]))  # 4
    print(t.maxTwoEvents([[1, 3, 2], [4, 5, 2], [1, 5, 5]]))  # 5
    print(t.maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]))  # 8
