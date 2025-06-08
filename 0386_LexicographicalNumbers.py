# Problem 386
from typing import List


class LexicographicalNumbers:

    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int, sorted(list(map(str, list(range(1, n + 1)))))))
