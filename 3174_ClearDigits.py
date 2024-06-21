# Problem 3174. Clear Digits
class BiweeklyContest132P1:
    def do_nothing(self):
        pass

    def clearDigits(self, s: str) -> str:
        stack = []
        digits = "0123456789"
        for ch in s:
            if ch in digits:
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ch)

        return "" if len(stack) == 0 else "".join(stack)
            
                



if __name__ == '__main__':
    b = BiweeklyContest132P1()
    print(b.clearDigits("abc"))
    print(b.clearDigits("cb34"))
    print(b.clearDigits(""))
    print(b.clearDigits("34"))
