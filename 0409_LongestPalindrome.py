# Problem 409
import collections


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> int:
        result, my_dict = 0, collections.Counter(s)
        odd_exists = False
        for k, v in my_dict.items():
            if v % 2 == 1:
                result += v - 1
                odd_exists = True
            else:
                result += v
        return result + (1 if odd_exists else 0)


if __name__ == '__main__':
    l = LongestPalindrome()
    print(l.longestPalindrome("bb"))
