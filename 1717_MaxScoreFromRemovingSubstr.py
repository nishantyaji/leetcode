# Problem 1717

class MaxScoreFromRemovingSubstr:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        start, result, diff = 0, 0, len("ba")
        [first, second] = ["ab", "ba"] if x > y else ["ba", "ab"]

        found = True
        while found:
            found, start = False, 0
            while True:
                try:
                    i = s.index(first, start)
                    s = s[:i] + s[i + diff:]
                    found, start = True, i
                    result += max(x, y)
                except ValueError:
                    break

        found = True
        while found:
            found, start = False, 0
            while True:
                try:
                    i = s.index(second, start)
                    s = s[:i] + s[i + diff:]
                    found, start = True, i
                    result += min(x, y)
                except ValueError:
                    break

        return result


if __name__ == '__main__':
    m = MaxScoreFromRemovingSubstr()
    print(m.maximumGain("cdbcbbaaabab", 4, 5))
    print(m.maximumGain("aabbaaxybbaabb", 5, 4))
