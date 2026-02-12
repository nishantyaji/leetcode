# Problem 3713

class LongestBalancedSubstringI:
    def longestBalanced(self, s: str) -> int:
        dicts = []

        def diff(d1: dict, d2: dict) -> bool:
            d3 = d1.copy()
            for k, v in d2.items():
                d3[k] -= v
                if d3[k] == 0:
                    del d3[k]
            vals = set(d3.values())
            if len(vals) == 1:
                return list(vals)[0] * len(d3)
            else:
                return 0

        dicts.append({})

        for c in s:
            d = dicts[-1].copy()
            if c not in d:
                d[c] = 0
            d[c] += 1
            dicts.append(d)

        mx = 1
        for i in range(0, len(s) - 1):
            for j in range(i + 2, len(s) + 1):
                val = diff(dicts[j], dicts[i])
                mx = max(mx, val)
        return mx