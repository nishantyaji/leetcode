# Problem 38


class CountAndSay:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)
        prev_ch, count, res = "~", 0, ""
        for c in s:
            if c == prev_ch:
                count += 1
            else:
                if prev_ch != "~":
                    res += (str(count) + prev_ch)
                prev_ch = c
                count = 1
        if count >= 1:
            res += (str(count) + prev_ch)
        return res
