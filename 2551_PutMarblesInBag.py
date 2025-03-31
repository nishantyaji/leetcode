# Problem 2551
from typing import List


class PutMarblesInBag:

    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        splits, k = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)]), k - 1
        return sum(splits[-k:]) - sum(splits[:k])


if __name__ == '__main__':
    p = PutMarblesInBag()
    print(p.putMarbles([25,74,16,51,12,48,15,5], 1))  # 0
    print(p.putMarbles([1, 4, 2, 5, 2], 3))  # 3
    print(p.putMarbles([1, 3, 5, 1], 2))  # 4
    print(p.putMarbles([1, 3], 2))  # 0
