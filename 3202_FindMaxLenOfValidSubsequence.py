# Problem 3202
from typing import List


class FindMaxLenOfValidSubsequence:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mp = dict()
        for i in range(k):
            mp[i] = dict()
        max_len = -1
        for n in nums:
            for i in range(k):
                n2 = n % k
                compl = (i - n2) % k
                mp[i][n2] = 1 if compl not in mp[i] else (mp[i][compl] + 1)
                max_len = max(max_len, mp[i][n2])
        return max_len


if __name__ == '__main__':
    f = FindMaxLenOfValidSubsequence()
    print(f.maximumLength([1, 2, 3, 4, 5], 2))
    print(f.maximumLength([1, 4, 2, 3, 1, 4], 3))
