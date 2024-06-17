# Problem 1208


class GetEqSubstringsWithinBudget:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_str, run_sum, i, j = 0, 0, 0, 0
        while i < len(s) and j < len(s):
            run_sum += abs(ord(s[j]) - ord(t[j]))
            if run_sum > maxCost:
                run_sum -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            else:
                max_str = max(max_str, j - i + 1)
            j += 1
        return max_str


if __name__ == '__main__':
    g = GetEqSubstringsWithinBudget()
    print(g.equalSubstring("krrgw", "zjxss", 19))
    # 2
    print(g.equalSubstring("anryddgaqpjdw", "zjhotgdlmadcf", 5))
    # 1
