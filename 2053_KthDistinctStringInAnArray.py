# Problem 2053
from typing import List


class KthDistinctStringInAnArray:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ones, more = [], set()

        for i in arr:
            if i in more:
                continue
            elif i in ones:
                ones.remove(i)
                more.add(i)
            else:
                ones.append(i)

        return "" if k > len(ones) else ones[k - 1]
