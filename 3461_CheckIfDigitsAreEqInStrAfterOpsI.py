# Problem 3461

class CheckIfDigitsAreEqInStrAfterOpsI:
    def hasSameDigits(self, s: str) -> bool:
        def do_op(s1: str):
            res1 = ""
            for i in range(len(s1) - 1):
                res1 += str((int(s1[i]) + int(s1[i + 1])) % 10)
            return res1

        if len(s) <= 1:
            return False
        while len(s) > 2:
            s = do_op(s)
        return s[0] == s[1]
