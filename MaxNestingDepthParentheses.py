# Problem 1614

class MaxNestingDepthParantheses:
    def maxDepth(self, s: str) -> int:
        maxval = 0
        running = 0
        for ch in s:
            if ch == "(":
                running += 1
                if maxval < running:
                    maxval = running
            elif ch == ")":
                running -= 1
        return maxval
