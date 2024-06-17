# Problem 1915
import collections
import math


class NumOfWonderfulSubstrings:

    def wonderfulSubstrings(self, word: str) -> int:
        dp = [None] * (len(word) + 1)
        my_dict = {}
        count = 0

        for ch in "abcdefghij":
            my_dict[ch] = int(pow(2, count))
            count += 1

        dp[0] = 0
        i = 1

        bit_dict = collections.defaultdict(int)
        bit_dict[0] = 1
        for ch in word:
            dp[i] = self.add(ch, dp[i - 1], my_dict)
            bit_dict[dp[i]] += 1
            i += 1

        keys = list(bit_dict.keys())
        keys.sort()

        result = 0
        visited = set()
        for i in keys:
            result += int((bit_dict[i] * (bit_dict[i] - 1)) / 2)
            for j in range(0, 10):
                to_add = int(pow(2, j))
                k = i + to_add
                if k not in visited and k in bit_dict and self.check_if_differ_one(i, k):
                    result += bit_dict[i] * bit_dict[k]
                k = i - to_add
                if k not in visited and k in bit_dict and self.check_if_differ_one(i, k):
                    result += bit_dict[i] * bit_dict[k]
            visited.add(i)

        return result

    def add(self, alph: str, num: int, my_dict: dict) -> int:
        return num ^ my_dict[alph]

    def check_if_differ_one(self, num1: int, num2: int) -> bool:
        res = num1 ^ num2
        base = int(math.log2(res))
        return res == pow(2, base)


if __name__ == '__main__':
    n = NumOfWonderfulSubstrings()
    print(n.wonderfulSubstrings("aaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(n.wonderfulSubstrings("he"))
    print(n.wonderfulSubstrings("aabb"))
