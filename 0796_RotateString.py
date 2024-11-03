# Problem 796

class RotateString:
    def rotateString(self, s: str, goal: str) -> bool:
        ss = s + s
        for i in range(len(s)):
            if ss[i:i + len(s)] == goal:
                return True
        return False
