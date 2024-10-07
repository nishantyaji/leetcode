# Problem 2696

class MinStrLenAfterRemovingSubstrings:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if (c == "D" and stack[-1] == "C") or (c == "B" and stack[-1] == "A"):
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)
