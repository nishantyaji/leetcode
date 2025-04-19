# Problem 89
from typing import List


class GrayCode:

    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        temp = self.grayCode(n - 1)
        return temp + [(pow(2, n - 1) + x) for x in temp[::-1]]
