# Problem 179
import functools
from typing import List


class LargestNumber:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_n(s1: str, s2: str):
            return -1 if s1 + s2 < s2 + s1 else 1

        return "".join(sorted(list(map(str, nums)), key=functools.cmp_to_key(compare_n), reverse=True))


if __name__ == '__main__':
    l = LargestNumber()
    print(l.largestNumber([111311, 1113]))
    print(l.largestNumber([3, 30, 34, 5, 9]))
    print(l.largestNumber([8308, 8308, 830]))  # "83088308830"
