# Problem 696

class CountBinSubstrings:

    def countBinarySubstrings(self, s: str) -> int:
        prev, count = "~", 0
        res = []
        for c in s:
            if c != prev:
                if prev != "~":
                    res.append(count)
                count = 1
            else:
                count += 1
            prev = c
        res.append(count)
        answer = 0
        for i in range(1, len(res)):
            answer += min(res[i - 1], res[i])
        return answer
