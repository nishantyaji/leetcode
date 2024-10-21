# Problem 1593
import copy


class SplitStringMaxNumUniqSubstr:
    def maxUniqueSplit(self, s: str) -> int:
        res, st = [0], set()
        self.recur(s, st, res)
        return res[0]

    def recur(self, remain: str, st: set, res: list[int]):
        if not remain:
            if res[0] < len(st):
                res[0] = len(st)
            return

        for i in range(1, len(remain) + 1):
            chosen = remain[:i]
            if chosen not in st:
                st_copy = copy.deepcopy(st)
                st_copy.add(chosen)
                self.recur(remain[i:], st_copy, res)
