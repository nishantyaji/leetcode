# Problem 1526
from typing import List


class MinNumIncOnSubarrToFormTargetArr:
    def minNumberOperations(self, target: List[int]) -> int:
        stack, res = [], 0
        for i, t in enumerate(target):
            if not stack or t > stack[-1]:
                stack.append(t)
            else:
                while stack and stack[-1] >= t:
                    popped = stack.pop()
                    to_remove = t
                    if stack and stack[-1] > t:
                        to_remove = stack[-1]
                    res += (popped - to_remove)
                stack.append(t)
        while stack:
            popped = stack.pop()
            to_remove = 0 if not stack else stack[-1]
            res += (popped - to_remove)
        return res


if __name__ == '__main__':
    m = MinNumIncOnSubarrToFormTargetArr()
    print(m.minNumberOperations([3, 1, 5, 4, 2]))  # 7
    print(m.minNumberOperations([1, 2, 3, 2, 1]))  # 3
    print(m.minNumberOperations([3, 1, 1, 2]))  # 4
