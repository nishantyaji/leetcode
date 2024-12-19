# Problem 769
import sys
from typing import List


class MaxChunksToMakeSorted:

    def maxChunksToSorted(self, arr: List[int]):
        prefix_max, suffix_min = [], []
        # for cut, it is required that max before is less than present
        # and min after should be greater than present
        mx, mn = -1, sys.maxsize
        for i in range(len(arr)):
            mx = max(mx, arr[i])
            mn = min(mn, arr[-1 - i])
            prefix_max.append(mx)
            suffix_min.append(mn)
        suffix_min.reverse()

        chunk = 0
        for i in range(len(arr)):
            if i == 0 and arr[i] == 0:
                chunk += 1
            elif 0 < i < len(arr) - 1 and prefix_max[i] <= i < suffix_min[i + 1]:
                chunk += 1
            elif i == len(arr) - 1 and prefix_max[i] <= i:
                chunk += 1
        return min(chunk, len(arr))

    def maxChunksToSorted_slow(self, arr: List[int]) -> int:
        # Using bit operations. Slow.
        nums = list(range(pow(2, len(arr) - 1)))
        bs = list(map(lambda x: x.bit_count(), nums))
        tuples = list(zip(bs, nums))
        tuples.sort(key=lambda x: (-x[0], -x[1]))
        b_len = len(arr) - 1

        def get_indices(numm):
            b = format(numm, "b").rjust(b_len, "0")
            return [i + 1 for i in range(b_len) if b[i] == "1"] + [b_len + 1]

        def check(indices):
            possible, mn, mx, prev, idx, i = True, sys.maxsize, -1, 0, 0, 0,
            while i <= b_len:
                if i == indices[idx]:
                    idx += 1
                    if mn != prev or mx != i - 1:
                        possible = False
                        break
                    else:
                        prev = mx + 1
                        mn, mx = sys.maxsize, -1
                else:
                    mn, mx = min(mn, arr[i]), max(mx, arr[i])
                    i += 1
            return possible

        for (bit_cnt, num) in tuples:
            indexes = get_indices(num)
            if check(indexes):
                return bit_cnt + 1


if __name__ == '__main__':
    m = MaxChunksToMakeSorted()
    print(m.maxChunksToSorted([0, 2, 1, 4, 3]))
    print(m.maxChunksToSorted([0, 1, 2, 3, 4]))
    print(m.maxChunksToSorted([2, 0, 1]))
    print(m.maxChunksToSorted([1, 0, 2, 3, 4]))
    print(m.maxChunksToSorted([4, 3, 2, 1, 0]))
