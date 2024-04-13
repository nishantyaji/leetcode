# Problem 131
from typing import List


class PalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        result_list = []
        self.recurse(s, [], result_list)
        return result_list

    def recurse(self, s: str, prefix: List[str], result_list: List[List[str]]):
        if len(s) == 0:
            result_list.append(prefix)
            return
        i = 0
        for j in range(i + 1, len(s) + 1):
            if self.is_palindrome(s[i:j]):
                prefix_copy = list(prefix)
                prefix_copy.append(s[i:j])
                self.recurse(s[j:], prefix_copy, result_list)

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]


if __name__ == '__main__':
    p = PalindromePartitioning()
    # print(p.is_palindrome("aabaa"))
    # print(p.is_palindrome("aa"))
    # print(p.is_palindrome("a"))
    # print(p.is_palindrome("aabaaa"))
    print(p.partition("aabaaa"))
    print(p.partition("aab"))
    # Output: [["a", "a", "b"], ["aa", "b"]]
    # print(p.partition("a"))
