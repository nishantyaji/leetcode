# Problem 632
import collections
import heapq
import sys
from collections import deque
from typing import List


class SmallestRangeCoveringElemsFromKLists_pq:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # had to look at hints to solve this

        dq, pq = deque(), []
        heapq.heapify(pq)
        max_val = -sys.maxsize
        for i, n in enumerate(nums):
            n = deque(n)
            val = n.popleft()
            max_val = max(max_val, val)
            heapq.heappush(pq, (val, i, n))

        res = sys.maxsize
        l_bound, u_bound = -sys.maxsize, -sys.maxsize
        while True:
            (min_val, min_group, arr) = heapq.heappop(pq)
            if max_val - min_val < res:
                res = max_val - min_val
                l_bound, u_bound = min_val, max_val
            if not arr:
                break
            temp = arr.popleft()
            heapq.heappush(pq, (temp, min_group, arr))
            max_val = max(max_val, temp)

        return [l_bound, u_bound]

    def smallestRange2(self, nums: List[List[int]]) -> List[int]:
        # This gives rise to TLE
        window = {}
        all_set = set(list(range(len(nums))))

        def add_(numm):
            if numm not in window:
                window[numm] = 0
            window[numm] += 1

        def rem_(numm):
            if numm in window:
                window[numm] -= 1
            if window[numm] == 0:
                del window[numm]

        def is_complete():
            return len(all_set - set(window.keys())) == 0

        dq = deque()
        pq = []
        heapq.heapify(pq)
        for i, n in enumerate(nums):
            heapq.heappush(pq, (n[0], i, n))

        res, l_bound, u_bound = sys.maxsize, -1, -1
        while pq:
            el = heapq.heappop(pq)
            add_(el[1])
            dq.append(el)
            while is_complete() or (dq and dq[-1][0] - dq[0][0] > res):
                if dq[-1][0] - dq[0][0] < res:
                    res = dq[-1][0] - dq[0][0]
                    l_bound, u_bound = dq[0][0], dq[-1][0]

                to_remove = dq.popleft()
                rem_(to_remove[1])
            if len(el[2]) > 1:
                # check if original group is empty or not
                heapq.heappush(pq, (el[2][1], el[1], el[2][1:]))

        return [l_bound, u_bound]

    def smallestRange3(self, nums: List[List[int]]) -> List[int]:
        # Gives rise to TLE
        merged = []
        for i in range(len(nums)):
            merged += [(x, i) for x in nums[i]]
        merged.sort(key=lambda x: (x[0], x[1]))
        num_num_set = set(list(range(len(nums))))
        window = {merged[0][1]: 1}

        def add_(numm):
            if numm not in window:
                window[numm] = 0
            window[numm] += 1

        def rem_(numm):
            if numm in window:
                window[numm] -= 1
                if window[numm] == 0:
                    del window[numm]

        def is_complete():
            return len(num_num_set - set(window.keys())) == 0

        left, right, res, l_bound, u_bound = 0, 0, sys.maxsize, -1, -1
        while right < len(merged):
            while merged[right][0] - merged[left][0] > res:
                rem_(merged[left][1])
                left += 1
            while is_complete():
                if merged[right][0] - merged[left][0] < res:
                    l_bound, u_bound = merged[left][0], merged[right][0]
                    res = merged[right][0] - merged[left][0]
                rem_(merged[left][1])
                left += 1
            right += 1
            if right < len(merged):
                add_(merged[right][1])
            else:
                if left < len(merged):
                    rem_(merged[left][1])
                    left += 1

        return [l_bound, u_bound]


if __name__ == '__main__':
    s = SmallestRangeCoveringElemsFromKLists_pq()
    print(s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
    print(s.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
