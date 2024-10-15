# Problem 403
from typing import List


class FrogJump:
    def canCross(self, stones: List[int]) -> bool:
        co_map = {x: i for i, x in enumerate(stones)}
        length = len(stones)
        dp = [[-1 for c in range(length)] for r in range(length)]

        for i in range(length - 1):
            dp[length - 1][i] = stones[length - 1] - stones[i]

        for x in range(length - 1, -1, -1):
            for y in range(x, -1, -1):
                if dp[x][y] > -1:
                    # If the frog landed in x from y
                    # then the jump is stones[x] - stones[y]
                    # We backtrack towards 0
                    # So we check if stones[y] - (jump|jump-1|jump+1) are valid stones
                    # if yes: say stones[y] - j is valid
                    # then we set dp[y][co_map[stones[y] - j] as a proper value and so on
                    jump = dp[x][y]
                    for j in [jump - 1, jump, jump + 1]:
                        if stones[y] - j in co_map:
                            dp[y][co_map[stones[y] - j]] = stones[y] - stones[co_map[stones[y] - j]]
        return dp[0][0] > -1


if __name__ == '__main__':
    f = FrogJump()
    print(f.canCross([0, 1, 3, 5, 6, 8, 12, 17]))
    print(f.canCross([0, 1, 2, 3, 4, 8, 9, 11]))
