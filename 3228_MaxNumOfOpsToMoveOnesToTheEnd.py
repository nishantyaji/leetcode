# Problem 3228


class MaxNumOfOpsToMoveOnesToTheEnd:
    def maxOperations(self, s: str) -> int:
        news, prev = "", "-"
        for c in s:
            if prev == '0' and c == '0':
                continue
            news += c
            prev = c
        s, count, arr = news, 0, []
        for c in s:
            if c == '0':
                arr.append(count)
                count = 0
            else:
                count += 1

        l, res = len(arr), 0
        for i, a in enumerate(arr):
            res += (l - i) * a
        return res
