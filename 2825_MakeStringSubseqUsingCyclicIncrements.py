# Problem 2825


class MakeStringSubseqUsingCyclicIncrements:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        def inc_string(s: str):
            return "".join(list(map(lambda c: chr(ord('a') + (ord(c) - ord('a') + 1) % 26), list(s))))

        str1inc = inc_string(str1)
        return True if self.is_subsequence(str1, str1inc, str2) else False

    def is_subsequence(self, parent: str, parent_inc: str, child: str):
        c_idx = 0
        for i, ch in enumerate(parent):
            if child[c_idx] == ch or child[c_idx] == parent_inc[i]:
                c_idx += 1
                if c_idx == len(child):
                    return True
        return c_idx == len(child)


if __name__ == '__main__':
    m = MakeStringSubseqUsingCyclicIncrements()
    print(m.canMakeSubsequence("abc", "ad"))
    print(m.canMakeSubsequence("zc", "ad"))
    print(m.canMakeSubsequence("ab", "d"))
