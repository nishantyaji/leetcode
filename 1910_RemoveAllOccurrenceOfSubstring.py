# Problem 1910

class RemoveAllOccurrenceOfSubstring:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack, rp, lp = [], list(part)[::-1], len(part)
        for c in s:
            stack.append(c)
            ls = len(stack)
            if ls >= lp and stack[::-1][:lp] == rp:
                stack = stack[:ls - lp]
        return "".join(stack)
