# Problem 5

class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        [limits, max_length] = self.find_longest_palindrome(s)
        return s[limits[0]: limits[1] + 1]

    def find_longest_palindrome(self, s):
        if len(s) <= 1:
            return [0, len(s)]

        max_length = 1
        limits = [0, 0]

        for i in range(1, len(s) - 1):
            count = 0
            for j in range(0, min(i, len(s) - i - 1) + 1):
                if s[i - j] != s[i + j]:
                    if count * 2 - 1 > max_length:
                        max_length = 2 * count - 1
                        limits = [i - j + 1, i + j - 1]
                        count = 0
                    break
                else:
                    count += 1
            if count > 0 and count * 2 - 1 > max_length:
                max_length = 2 * count - 1
                j = min(i, len(s) - i - 1)
                # limits = [i - j + 1, i + j - 1]
                limits = [i - j, i + j]

        for i in range(0, len(s) - 1):
            count = 0
            diff = -1
            for j in range(i + 1, len(s)):
                diff = j - (i + 1)
                if i - diff < 0 or s[i - diff] != s[j]:
                    if max_length < count:
                        max_length = count
                        limits = [i - diff + 1, j - 1]
                        count = 0
                    break
                else:
                    count += 2
            if max_length < count:
                max_length = count
                limits = [i - diff, i + diff + 1]

        return [limits, max_length]


if __name__ == '__main__':
    l = LongestPalindromicSubstring()
    print(l.longestPalindrome("babad"))
    print(l.longestPalindrome("cbbd"))