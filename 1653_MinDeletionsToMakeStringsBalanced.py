# Problem 1653
import itertools


class MinDeletionsToMakeStringsBalanced:
    def minimumDeletions(self, s: str) -> int:
        num_as = sum([1 for x in s if x == "a"])
        # Num of a's after an index
        a = list(map(lambda x: num_as - x, list(itertools.accumulate(map(lambda x: 1 if x == "a" else 0, s)))))
        # num of b's before an index
        b = [0] + list(itertools.accumulate(map(lambda x: 1 if x == "b" else 0, s)))
        return 0 if sum(a) == 0 or sum(b) == 0 else min([a[i] + b[i] for i in range(len(s))])


if __name__ == '__main__':
    m = MinDeletionsToMakeStringsBalanced()
    print(m.minimumDeletions("aababbab"))
    print(m.minimumDeletions("bbaaaaabb"))
    print(m.minimumDeletions(
        "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"))
