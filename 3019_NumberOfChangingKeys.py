# Problem 3019

class NumberOfChangingKeys:
    def countKeyChanges(self, s: str) -> int:
        to_u = ord('a') - ord('A')
        count = 0
        for i in range(1, len(s)):
            diff = ord(s[i]) - ord(s[i - 1])
            if diff == to_u or diff == -to_u or diff == 0:
                continue
            count += 1
        return count
