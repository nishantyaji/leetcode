#Problem 1745


class PalindromePartitioningIV:
    def checkPartitioning(self, s: str) -> bool:
        if len(s) < 3:
            return False
        if len == 3:
            return True

        return self.find_longest_palindrome(s)

    def find_longest_palindrome(self, s) -> bool:
        for i in range(1, len(s) - 1):
            for j in range(0, min(i, len(s) - i - 1) + 1):
                if s[i - j] != s[i + j]:
                    break
                else:
                    if self.is_palindrome(s[:(i-j)]) and self.is_palindrome(s[(i+j+1):]):
                        return True

        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                diff = j - (i + 1)
                if i - diff < 0 or s[i - diff] != s[j]:
                    break
                else:
                    if self.is_palindrome(s[:(i-diff)]) and self.is_palindrome(s[j+1:]):
                        return True

        return False

    def is_palindrome(self, s):
        return len(s) > 0 and s == s[::-1]

if __name__ == '__main__':
    p = PalindromePartitioningIV()
    print(p.checkPartitioning("abcbdd"))
    print(p.checkPartitioning("bcbddxy"))