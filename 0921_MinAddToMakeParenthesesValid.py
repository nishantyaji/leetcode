import collections


class MinAddToMakeParenthesesValid:
    def minAddToMakeValid(self, s: str) -> int:
        dq = collections.deque()
        count = 0
        for c in s:
            if c == ")":
                if not dq:
                    count += 1
                else:
                    dq.popleft()
            else:
                dq.append(c)

        return count + len(dq)