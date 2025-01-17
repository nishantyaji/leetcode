# Problem 2516
import sys


class TakeKOfEachCharFromLeftRight:

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        def val(ch):
            return ord(ch) - ord('a')

        vals, for_l, back_l = [0] * 3, sys.maxsize, sys.maxsize
        for i in range(len(s)):
            vals[val(s[i])] += 1
            if vals[0] >= k and vals[1] >= k and vals[2] >= k:
                for_l = i
                break

        if for_l == sys.maxsize:
            return -1

        vals = [0] * 3
        for i in range(len(s) - 1, -1, -1):
            vals[val(s[i])] += 1
            if vals[0] >= k and vals[1] >= k and vals[2] >= k:
                back_l = i
                break

        min_len = min(len(s) - back_l, for_l + 1)
        total_iter = len(s) - back_l + for_l + 1
        left, right = back_l, back_l-1
        vals = [0] * 3
        # Unclean code
        for _ in range(total_iter):
            right = (right + 1) % len(s)
            vals[val(s[right])] += 1
            while vals[0] >= k and vals[1] >= k and vals[2] >= k:
                min_len = min(min_len, right + len(s) - left + 1)
                vals[val(s[left])] -= 1
                left = (left + 1) % len(s)

        return min_len


if __name__ == '__main__':
    t = TakeKOfEachCharFromLeftRight()
    print(t.takeCharacters("ccbabcc", 1))
    print(t.takeCharacters("abc", 1))
    print(t.takeCharacters("aabaaaacaabc", 2))
    print(t.takeCharacters("a", 1))
