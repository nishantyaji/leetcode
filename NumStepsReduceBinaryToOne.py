# Problem 1404

class NumStepsReduceBinaryToOne:
    def numSteps(self, s: str) -> int:
        num = 0
        for ch in s:
            num = 2 * num + (ord(ch) - ord('0'))

        steps = 0
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num += 1
            steps += 1
        return steps
