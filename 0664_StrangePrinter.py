# Problem 664
import functools
import sys


class StrangePrinter:
    @functools.cache
    def strangePrinter(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        temp_min = sys.maxsize
        for i in range(1, len(s)):
            temp = self.strangePrinter(s[:i]) + self.strangePrinter(s[i:])
            if s[0] == s[i]:
                # if the leading character in the above 2 partitions then
                # remove 1
                # because they would as well have been one turn
                # All the combinations of same character are considered
                temp -= 1
            temp_min = min(temp, temp_min)

        return temp_min


if __name__ == '__main__':
    s = StrangePrinter()
    print(s.strangePrinter("aba"))
    # 2
    print(s.strangePrinter("dddccbdbababaddcbcaabdbdddcccddbbaabddb"))
    # 15
    print(s.strangePrinter("abcabc"))
    # 5
    print(s.strangePrinter("abcabcabc"))
    # 7
    print(s.strangePrinter("aaabbb"))
    # 2
