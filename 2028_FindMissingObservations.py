# Problem 2028
from typing import List


class FindMissingObservations:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rem = mean * (n + len(rolls)) - sum(rolls)
        if rem < n or rem > 6 * n:
            return []

        avg, r = divmod(rem, n)
        res = []
        for i in range(n):
            res.append(avg + (0 if i >= r else 1))
        return res
