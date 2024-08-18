# Problem 264
import bisect
import heapq


class UglyNumberII:

    def nthUglyNumber(self, n: int) -> int:
        q = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        q_set = set(q)
        if n <= len(q):
            return q[n - 1]
        pq = []
        heapq.heapify(pq)

        while n > len(q) - 1:
            for i in [2, 3, 5]:
                from_i = bisect.bisect_right(q, q[-1] // i)
                ans = q[from_i] * i
                if ans not in q_set:
                    heapq.heappush(pq, ans)
                    q_set.add(ans)
            q.append(heapq.heappop(pq))

        return q[n - 1]


if __name__ == '__main__':
    u = UglyNumberII()
    print(u.nthUglyNumber(1352))
    print(u.nthUglyNumber(10))
    print(u.nthUglyNumber(1))
