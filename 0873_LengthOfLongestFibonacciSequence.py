# Problem 873
import functools
from typing import List


class LengthOfLongestFibonacciSequence:

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mp = {x: i for i, x in enumerate(arr)}

        @functools.cache
        def recur(index_high: int, index_low) -> int:
            temp = arr[index_high] - arr[index_low]
            if temp in mp and temp < arr[index_low]:
                return 1 + recur(index_low, mp[temp])
            return 1

        mx = 0
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if arr[i] - arr[j] in mp and arr[i] - arr[j] < arr[j]:
                    mx = max(mx, 1 + recur(i, j))

        return mx


if __name__ == '__main__':
    l = LengthOfLongestFibonacciSequence()
    print(l.lenLongestFibSubseq([2392, 2545, 2666, 5043, 5090, 5869, 6978, 7293, 7795]))  # 0
    print(l.lenLongestFibSubseq([1, 3, 5]))  # 0
    print(l.lenLongestFibSubseq([2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34]))  # 5
    print(l.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))  # 5
    print(l.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))  # 3
