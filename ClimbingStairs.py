# Problem 70

class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]
        if n < 3:
            return ways[n - 1]
        for i in range(2, n):
            ways.append(ways[0] + ways[1])
            ways.pop(0)
        return ways[1]
