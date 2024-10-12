# Problem 3315
import functools
from typing import List


class ConstructMinBitwiseArrayII:

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        @functools.cache
        def solve(a: int) -> int:
            if a == 2:
                return -1
            b = format(a, 'b')
            i = 0
            while i <= len(b) - 1 and b[len(b) - 1 - i] == "1":
                i += 1
            if i == 1:
                return int(b[:len(b) - 1] + "0", 2)
            else:
                temp = "".join(["1"] * (i - 1))
                return int(b[:len(b) - i] + "0" + temp, 2)

        return [solve(x) for x in nums]


if __name__ == '__main__':
    c = ConstructMinBitwiseArrayI()
    print(c.minBitwiseArray([2, 3, 5, 7]))
    print(c.minBitwiseArray([11, 13, 31]))
