# Problem 3243
from typing import List


class ShortestDistanceAfterRoadAdditionQueriesI:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        out_v = {i: [i + 1] for i in range(n - 1)}
        dp = [i for i in range(n)]
        res = []
        for [s, e] in queries:
            dp[e] = min(dp[e], dp[s] + 1)
            out_v[s].append(e)
            self.update_all(dp, out_v, e)
            res.append(dp[n - 1])

        return res

    def update_all(self, dp: List[int], out_v: dict, v: int):
        if v in out_v and len(out_v[v]) > 0:
            for nei in out_v[v]:
                prev = dp[nei]
                dp[nei] = min(dp[nei], dp[v] + 1)
                # This below if block is important
                if prev != dp[nei]:
                    self.update_all(dp, out_v, nei)


if __name__ == '__main__':
    s = ShortestDistanceAfterRoadAdditionQueriesI()
    print(s.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))
    print(s.shortestDistanceAfterQueries(4, [[0, 3], [0, 2]]))
